
import json

def mark_traditional_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    keywords = [
        "Preparation", 
        "Ajax Refresh", 
        "Ajax Submit", 
        "Table Records", 
        "List Records", 
        "List_Navigation", 
        "Session Variable",
        "Notify"
    ]
    
    count = 0
    for q in data:
        # Check question text and options for keywords
        text_to_check = q['question'] + " " + " ".join([opt['text'] for opt in q['options']])
        
        is_traditional = False
        for kw in keywords:
            if kw.lower() in text_to_check.lower():
                is_traditional = True
                break
        
        if is_traditional:
            # Check if already marked
            if "[Traditional]" not in q['question']:
                q['question'] = f"[Traditional] {q['question']}"
                count += 1
                
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Marked {count} questions as [Traditional] in {file_path}")

mark_traditional_questions('structured_data.json')
