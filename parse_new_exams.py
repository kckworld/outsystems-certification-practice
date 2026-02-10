
import json
import re
import os

def parse_questions_file(file_path, stop_at_header=None):
    """
    Parses the question file (e.g., New_Practice_Exam.md or New_Practice_Exam_Scenairo.md).
    Extracts the updated logic where questions start with:
    - **문제 01. ...** (bold + '문제 ' prefix)
    - **01. ...** (bold + number)
    - 01. ...
    
    stop_at_header: If provided, stops parsing when a line containing this string is found.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return {}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # If stop_at_header is provided, truncate content
    if stop_at_header:
        parts = content.split(stop_at_header)
        content = parts[0]

    # Split by double newlines or lines that look like a header
    lines = content.split('\n')
    
    questions_map = {}
    current_q_id = None
    current_q_text = ""
    current_options = []
    
    # Regex for question start: 
    # Matches "**문제 01." or "**01." or "01." or "문제 01."
    # Group 2 is the ID, Group 3 is the text
    q_start_pattern = re.compile(r'^\**\s*(문제\s*)?(\d+)\.\s*(.*?)(\**)?$')
    
    # Regex for options: Matches "A. " or "A) "
    opt_pattern = re.compile(r'^([A-D])[\.\)]\s*(.*)')

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a question start
        q_match = q_start_pattern.match(line)
        if q_match:
            # Save previous question if exists
            if current_q_id:
                questions_map[current_q_id] = {
                    "question": current_q_text,
                    "options": current_options
                }
            
            # Reset for new question
            current_q_id = str(int(q_match.group(2))) # Normalize "01" to "1"
            # Remove any trailing ** if present in the text group or separate
            current_q_text = q_match.group(3).strip().rstrip('*')
            current_options = []
            continue
        
        # Check if line is an option
        opt_match = opt_pattern.match(line)
        if opt_match and current_q_id:
            current_options.append({
                "code": opt_match.group(1),
                "text": opt_match.group(2).strip()
            })
    
    # Add the last question
    if current_q_id:
        questions_map[current_q_id] = {
            "question": current_q_text,
            "options": current_options
        }
        
    return questions_map

def parse_answers_file(file_path, stop_at_header=None):
    """
    Parses the answer/explanation file.
    stop_at_header: If provided, stops parsing when a line containing this string is found.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return {}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # If stop_at_header is provided, truncate content
    if stop_at_header:
        parts = content.split(stop_at_header)
        content = parts[0]

    answers_map = {}
    
    # Strategy 1: Parse the ### headers with answers below them
    sections = re.split(r'\n### ', content)
    
    for section in sections:
        lines = section.strip().split('\n')
        if not lines:
            continue
            
        header = lines[0]
        id_match = re.search(r'(문제\s*)?(\d+)\.', header)
        if not id_match:
            id_match = re.match(r'^(\d+)(\.|\s|$)', header)
        
        if id_match:
            q_id = str(int(id_match.group(2) if len(id_match.groups()) > 1 else id_match.group(1)))
            
            answer_code = ""
            explanation_lines = []
            is_explanation = False
            
            for line in lines[1:]:
                line = line.strip()
                ans_match = re.search(r'\[x\]\s*\**([A-D])[\.\)]', line)
                if ans_match:
                    answer_code = ans_match.group(1)
                
                if "**Answer:" in line:
                    ans_text_match = re.search(r'\*\*Answer:\s*([A-D])', line)
                    if ans_text_match:
                        answer_code = ans_text_match.group(1)

                if "> **해설**" in line or "**해설**" in line:
                    is_explanation = True
                    continue
                
                if is_explanation:
                    # Skip section dividers and headers that might be caught in the split
                    if line.strip().startswith('---') or line.strip().startswith('##'):
                        continue
                        
                    if line.startswith(">"):
                        line = line.lstrip(">").strip()
                    explanation_lines.append(line)
            
            explanation = "\n".join(explanation_lines).strip()
            
            if q_id not in answers_map:
                answers_map[q_id] = {}
            
            if answer_code:
                answers_map[q_id]['answer_code'] = answer_code
            if explanation:
                answers_map[q_id]['explanation'] = explanation

    # Strategy 2: Parse Quick Answer Table
    tables = re.findall(r'\|.*\|\n\|[-|\s]+\|\n\|.*\|', content)
    for table in tables:
        lines = table.strip().split('\n')
        ids = [x.strip() for x in lines[0].strip('|').split('|')]
        ans = [x.strip().replace('①','A').replace('②','B').replace('③','C').replace('④','D') for x in lines[2].strip('|').split('|')]
        
        if len(ids) == len(ans):
            for i in range(len(ids)):
                if ids[i].isdigit():
                    q_id = str(int(ids[i]))
                    code = ans[i]
                    if q_id not in answers_map:
                        answers_map[q_id] = {}
                    if 'answer_code' not in answers_map[q_id] or not answers_map[q_id]['answer_code']:
                        answers_map[q_id]['answer_code'] = code

    return answers_map

def merge_and_save(questions_file, answers_file, output_file, stop_at_header=None):
    print(f"Processing {questions_file} + {answers_file} -> {output_file}")
    
    # Pass 'stop_at_header' to BOTH functions
    q_map = parse_questions_file(questions_file, stop_at_header)
    a_map = parse_answers_file(answers_file, stop_at_header)
    
    final_list = []
    
    # Iterate through sorted IDs from QUESTIONS file only
    all_ids = sorted([int(k) for k in q_map.keys()])
    
    for int_id in all_ids:
        qid = str(int_id)
        q_data = q_map[qid]
        a_data = a_map.get(qid, {})
        
        merged_item = {
            "id": qid,
            "question": q_data['question'],
            "options": q_data['options'],
            "answer_code": a_data.get('answer_code', ""),
            "explanation": a_data.get('explanation', "")
        }
        final_list.append(merged_item)
        
    print(f"Total merged questions: {len(final_list)}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_list, f, ensure_ascii=False, indent=2)

# --- Main Execution ---

# 1. New Practice Exam
# Stop parsing when "고난도 시나리오 모의고사" header is found in BOTH question and answer files
# This is more specific than "고난도 시나리오" which appears in the quick answer table header
merge_and_save(
    'New_Practice_Exam.md', 
    'New_Practice_Exam_Answer.md', 
    'new_exam_data.json',
    stop_at_header="고난도 시나리오 모의고사" 
)

# 2. Scenario Exam
merge_and_save(
    'New_Practice_Exam_Scenairo.md',
    'New_Practice_Exam_Scenairo_Answer.md',
    'scenario_exam_data.json'
)
