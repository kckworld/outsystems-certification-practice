## 📝 OutSystems 11 Associate Reactive 모의고사 (50문항)

### **[Part 1. UI 디자인 (UI Design) - 13문항]**

**문제 01. Input 위젯 사용 시 사용자가 입력한 데이터를 저장하기 위해 필수적으로 설정해야 하는 속성은?**
A. Name
B. Variable
C. Input Type
D. Prompt

**문제 02. Expression 위젯에서 HTML 태그가 포함된 텍스트를 실제 서식(굵게, 기울임 등)으로 렌더링하고 싶을 때 설정값은?**
A. Escape Content = Yes
B. Escape Content = No
C. Extended Properties = "html"
D. Value = "text/html"

**문제 03. Form 위젯 내부에 있는 모든 위젯의 유효성 여부(에러 발생 여부)를 한 번에 확인할 수 있는 속성은?**
A. Form.Valid
B. Form.IsDirty
C. Form.Validation
D. Form.Empty

**문제 04. Label 위젯을 특정 Input 위젯과 연결(Input Widget 속성 지정)했을 때의 장점은?**
A. Label을 클릭하면 연결된 Input 위젯으로 포커스가 이동한다.
B. Input 위젯의 데이터 타입이 자동으로 결정된다.
C. 화면 로딩 속도가 빨라진다.
D. Input 위젯의 값이 Label에 자동으로 복사된다.

**문제 05. Web Block이 자신의 데이터를 부모 화면(Screen)으로 전달하기 위해 사용하는 매커니즘은?**
A. Output Parameters
B. Events
C. Screen Variables
D. Input Parameters

**문제 06. Web Block 내부에서 정의된 Local Variable에 대한 설명으로 옳은 것은?**
A. 부모 화면에서 직접 읽고 수정할 수 있다.
B. 오직 해당 Web Block 내부에서만 접근 가능하다.
C. Client Variable로 자동 변환된다.
D. 다른 Web Block에서도 공유하여 사용할 수 있다.

**문제 07. Web Block의 'On Parameters Changed' 이벤트는 어떤 경우에 트리거되는가?**
A. 블록 내부에서 로컬 변수 값을 변경했을 때
B. 부모 화면이 블록의 Input Parameter에 전달하는 값을 변경했을 때
C. 블록이 처음으로 렌더링될 때
D. 블록 내의 버튼을 클릭했을 때

**문제 08. Placeholder 위젯의 주요 역할은 무엇인가?**
A. Web Block 내부에 부모 화면이 원하는 위젯을 넣을 수 있는 공간을 제공한다.
B. 데이터가 로딩되는 동안 보여주는 이미지이다.
C. SQL 쿼리의 매개변수 값을 저장한다.
D. 텍스트 입력창 안에 흐리게 나타나는 안내 문구이다.

**문제 09. Button 위젯의 'Built-in Validation'이 True일 때, 유효성 검사는 어느 시점에 발생하는가?**
A. 화면이 처음 로드될 때
B. 버튼을 클릭하여 로직이 실행되기 직전
C. 서버 액션이 완료된 직후
D. 데이터베이스에 값이 저장된 후

**문제 10. Table 위젯에서 특정 행(Row)을 클릭했을 때 이벤트를 처리하기 가장 적합한 방식은?**
A. 행의 `On Click` 이벤트에 Client Action을 연결한다.
B. Aggregate의 `On After Fetch`를 사용한다.
C. 화면의 `On Render` 이벤트를 사용한다.
D. Table의 `Header` 속성을 수정한다.

**문제 11. Dropdown 위젯에 표시될 리스트 데이터를 지정하는 속성은?**
A. Variable
B. List
C. Values
D. Source

**문제 12. 로직의 결과에 따라 화면에 동적으로 텍스트를 출력할 때 사용하는 가장 적합한 위젯은?**
A. Text
B. Label
C. Expression
D. Container

**문제 13. Checkbox 위젯과 바인딩(연결)되어야 하는 변수의 데이터 타입은?**
A. Integer
B. Text
C. Boolean
D. Decimal

---

### **[Part 2. 로직 (Logic) - 11문항]**

**문제 14. Client Action 내부에서 Server Action을 호출하는 것에 대한 설명으로 옳은 것은?**
A. 가능하다.
B. 불가능하다.
C. 오직 오프라인 모드에서만 가능하다.
D. Service Center 설정을 통해서만 가능하다.

**문제 15. Server Action 내부에서 Client Action을 호출하는 것에 대한 설명으로 옳은 것은?**
A. 가능하다.
B. 불가능하다.
C. 입력 파라미터가 없는 경우에만 가능하다.
D. 시스템 액션을 통해서만 가능하다.

**문제 16. Client Action 내에서 Database Entity에 직접 데이터를 생성(Create)할 수 있는가?**
A. 예, 직접 접근이 가능하다.
B. 아니요, 반드시 Server Action이나 Aggregate를 통해야 한다.
C. 오직 관리자 계정일 때만 가능하다.
D. 화면의 Aggregate가 At Start일 때만 가능하다.

**문제 17. Logic Flow에서 특정 조건(True/False)에 따라 실행 경로를 나눌 때 사용하는 노드는?**
A. Assign
B. If
C. Switch
D. For Each

**문제 18. Exception Handler 노드에서 'Abort Transaction' 속성을 Yes로 설정하면 어떻게 되는가?**
A. 현재 에러를 무시하고 다음 로직을 실행한다.
B. 발생한 데이터 변경 사항을 모두 취소(Rollback)한다.
C. 사용자를 로그아웃시킨다.
D. 에러 로그를 서버에 기록하지 않는다.

**문제 19. 서버 통신(Request) 없이 브라우저 메모리 내에서만 즉시 실행되는 액션의 종류는?**
A. Server Action
B. Client Action
C. Data Action
D. Service Action

**문제 20. Form.Valid 값이 False일 때, 버튼 클릭 시 연결된 액션 로직의 동작은?**
A. 플랫폼이 로직 실행을 자동으로 차단한다.
B. 개발자가 If 노드로 Form.Valid를 체크하여 로직 실행 여부를 직접 제어해야 한다.
C. 에러 메시지만 보여주고 로직은 정상 실행된다.
D. 화면이 자동으로 새로고침된다.

**문제 21. 로직 실행 중 특정 상황(예: 재고 부족)에서 에러를 강제로 발생시키고 싶을 때 사용하는 노드는?**
A. Raise Exception
B. Exception Handler
C. End
D. Assign

**문제 22. 'Function' 속성이 Yes인 액션이 가질 수 있는 Output Parameter의 개수 제한은?**
A. 0개
B. 반드시 1개
C. 무제한
D. 최대 5개

**문제 23. 액션 내에서 리스트의 특정 위치(인덱스)에 데이터를 삽입하고 싶을 때 사용하는 시스템 액션은?**
A. ListAppend
B. ListInsert
C. ListRemove
D. ListFilter

**문제 24. Input Parameter의 Mandatory 속성이 True일 때, 호출자가 값을 넘기지 않으면?**
A. 기본값이 자동으로 들어간다.
B. 디자인 타임(Service Studio)에서 에러가 발생한다.
C. 런타임에 경고만 표시된다.
D. 해당 파라미터는 무시된다.

---

### **[Part 3. 데이터 페칭 (Data Fetching) - 10문항]**

**문제 25. Aggregate에서 두 엔티티를 연결할 때, 왼쪽(기준) 엔티티의 모든 데이터를 포함하는 조인 방식은?**
A. Only With
B. With or Without
C. With
D. Full Join

**문제 26. Aggregate에서 특정 조건(예: 가격 > 1000)에 맞는 데이터만 가져오기 위해 사용하는 탭은?**
A. Sources
B. Filters
C. Sorting
D. Test

**문제 27. Aggregate의 결과를 화면의 Table 위젯에 표시하려면 위젯의 어느 속성에 연결해야 하는가?**
A. Variable
B. Source
C. List
D. Value

**문제 28. 화면 로드 시가 아니라, 특정 버튼 클릭 시에만 데이터를 가져오도록 설정하는 Fetch 값은?**
A. At start
B. Only on demand
C. On Render
D. After Initialize

**문제 29. Screen Aggregate와 Data Action의 실행 순서에 대한 설명으로 옳은 것은?**
A. Aggregate가 항상 먼저 실행된다.
B. Data Action이 항상 먼저 실행된다.
C. 순서가 없으며 비동기적으로 동시에 실행된다.
D. 화면에 정의된 순서(위에서 아래로)대로 실행된다.

**문제 30. Aggregate 내에서 특정 컬럼의 합계(Sum)나 평균(Average)을 계산하는 방법은?**
A. 계산할 수 없다. SQL 위젯을 써야 한다.
B. 속성을 우클릭하여 'Average' 또는 'Sum' 함수를 적용한다.
C. For Each 루프를 사용하여 직접 계산해야 한다.
D. Client Variable에 저장한 후 계산한다.

**문제 31. Aggregate에서 동적 정렬(Dynamic Sort)을 위해 정렬 탭에 작성하는 올바른 형식은?**
A. "{Entity}.[Attribute]"
B. "Entity.Attribute"
C. "{Entity}.{Attribute}"
D. "Sort(Attribute)"

**문제 32. 화면의 'On After Fetch' 이벤트가 발생하는 시점은?**
A. 데이터 요청을 보내기 직전
B. 데이터 페칭(Aggregate/Data Action)이 성공적으로 완료된 직후
C. 화면이 처음 렌더링될 때
D. 데이터베이스 서버가 재시작될 때

**문제 33. Aggregate 결과 리스트가 비어있는지 로직에서 확인하기 위해 사용하는 리스트 속성은?**
A. List.Empty
B. List.Count = 0
C. List.IsSet
D. List.Null

**문제 34. Data Action이 Screen Aggregate와 비교하여 가지는 주요 차이점은?**
A. 실행 속도가 훨씬 빠르다.
B. 여러 개의 Output Parameter를 반환할 수 있다.
C. DB에 직접 데이터를 수정(Write)할 수 있다.
D. 서버 액션을 호출할 수 없다.

---

### **[Part 4. 데이터 모델링 (Data Modelling) - 6문항]**

**문제 35. Entity Identifier가 Long Integer 타입일 때, 데이터 삽입 시 ID가 자동 증가되는 속성은?**
A. Is Unique
B. Is Autonumber
C. Mandatory
D. Default Value

**문제 36. Static Entity의 레코드를 애플리케이션 실행 중(Runtime)에 사용자가 추가할 수 있는가?**
A. 예, 일반 엔티티처럼 가능하다.
B. 아니요, 디자인 타임(Service Studio)에서만 정의 가능하다.
C. 관리자 권한이 있는 경우에만 가능하다.
D. 엑셀 업로드 기능을 통해서만 가능하다.

**문제 37. 두 엔티티 간의 일대다(1:N) 관계에서 외래 키(Foreign Key) 속성이 위치해야 하는 곳은?**
A. '1' 쪽 엔티티
B. 'N' 쪽 엔티티
C. 별도의 중간 연결 엔티티
D. 양쪽 엔티티 모두

**문제 38. Delete Rule이 'Protect'일 때, 자식 레코드가 있는 부모 레코드를 삭제하려고 하면?**
A. 부모와 자식 레코드가 모두 삭제된다.
B. 에러가 발생하며 삭제가 중단된다.
C. 부모 레코드만 삭제되고 자식은 유지된다.
D. 자식 레코드의 외래 키가 Null로 자동 변경된다.

**문제 39. 엔티티 속성에 'Unique Index'를 설정했을 때 발생하는 효과는?**
A. 해당 속성에 중복된 값이 저장되는 것을 방지한다.
B. 해당 속성을 자동으로 기본 키(PK)로 만든다.
C. 데이터 검색 속도가 매우 느려진다.
D. 해당 속성을 반드시 필수(Mandatory)로 만든다.

**문제 40. Static Entity가 생성될 때 기본적으로 포함되는 속성(Attribute)이 아닌 것은?**
A. Id
B. Label
C. Order
D. CreatedBy

---

### **[Part 5. 리액티브 앱 & 라이프사이클 - 6문항]**

**문제 41. 화면 전환 시 가장 먼저 발생하는 라이프사이클 이벤트는?**
A. On Ready
B. On Initialize
C. On Render
D. On After Fetch

**문제 42. 브라우저의 DOM이 완전히 생성되어 위젯 조작이 가능해진 시점에 발생하는 이벤트는?**
A. On Initialize
B. On Ready
C. On Render
D. On Destroy

**문제 43. Client Variable의 값 유지 기간에 대한 설명으로 옳은 것은?**
A. 브라우저 탭을 닫으면 즉시 소멸한다.
B. 브라우저를 종료해도 값이 유지된다 (기기/브라우저 로컬 저장).
C. 서버를 재시작할 때마다 초기화된다.
D. 보안을 위해 30분마다 자동으로 삭제된다.

**문제 44. Client Variable에 저장할 수 있는 데이터 타입에 대한 설명으로 옳은 것은?**
A. 기본 타입(Text, Integer, Boolean 등)만 가능하다.
B. 리스트(List)와 구조체(Structure)도 저장 가능하다.
C. 이미지와 같은 바이너리(Binary Data)만 가능하다.
D. OutSystems의 모든 데이터 타입을 지원한다.

**문제 45. On Initialize 이벤트 내에서 Server Action을 호출하는 행위에 대한 평가는?**
A. 권장된다 (데이터를 가장 빨리 가져올 수 있음).
B. 지양해야 한다 (응답을 기다리는 동안 화면 렌더링이 멈춤).
C. 필수적이다 (화면 보안을 위해).
D. 오프라인 모드에서만 가능하다.

**문제 46. 화면 데이터가 변경되어 UI가 다시 그려질 때마다 반복적으로 실행되는 이벤트는?**
A. On Ready
B. On Render
C. On Initialize
D. On After Fetch

---

### **[Part 6. 아키텍처 & 보안 - 4문항]**

**문제 47. Producer 모듈의 요소를 Consumer 모듈에서 참조하여 사용하려면 설정해야 하는 속성은?**
A. Public = Yes
B. Expose = Yes
C. Shared = Yes
D. Global = Yes

**문제 48. Producer 모듈의 서버 액션 '내부 로직'만 수정했을 때, Consumer 모듈의 상태는?**
A. 반드시 수동으로 다시 배포(Publish)해야 반영된다.
B. 다시 배포하지 않아도 런타임에 즉시 최신 로직이 반영된다.
C. Consumer 모듈에 'Outdated' 에러가 발생하여 실행이 멈춘다.
D. 서비스 센터에서 직접 동기화 버튼을 눌러야 한다.

**문제 49. 특정 화면을 '로그인한 사용자'만 접근 가능하게 하려면 Roles에서 무엇을 해제해야 하는가?**
A. Registered
B. Anonymous
C. Admin
D. Everyone

**문제 50. 사용자가 특정 Role(예: Manager)을 가졌는지 로직 내에서 확인하기 위해 사용하는 함수는?**
A. GetRole()
B. Check<RoleName>Role()
C. HasRole()
D. UserHasAccess()

---

**문제를 다 푸셨다면 말씀해 주세요! 1번부터 50번까지 정답과 상세 해설을 공개하겠습니다.** 과락 없이 70점(35문제) 이상 맞히시는 것을 목표로 해보세요! 🚀


그렇습니다. 아웃시스템즈 자격증 시험은 단순 암기보다는 **"이 상황에서 로직이 어떻게 흐르는가?"** 또는 **"이 설정을 바꿨을 때 어떤 사이드 이펙트가 발생하는가?"**를 묻는 시나리오형 문제가 고난도로 출제됩니다.

SI 실무 경험이 있으신 분들이 특히 낚이기 쉬운 **'예외 케이스'**와 **'복합 개념'**을 섞어서 20문제를 엄선했습니다. 이번에는 보기 하나하나가 정답처럼 느껴질 수 있으니 주의 깊게 풀어보세요.

---

## 🌪️ OutSystems Associate Reactive 고난도 시나리오 모의고사

### **[Part 1. UI & Lifecycle (심화)]**

**문제 01. Web Block 안에 또 다른 Web Block이 있고, 가장 안쪽 블록에서 이벤트를 발생시켰습니다. 부모 화면(Screen)에서 이 데이터를 받기 위한 올바른 과정은?**
A. 안쪽 블록의 이벤트는 자동으로 부모 화면까지 전달(Bubbling)되므로 화면에서 바로 핸들러를 연결한다.
B. 중간 블록이 안쪽 블록의 이벤트를 잡아서, 다시 자신의 이벤트를 발생시켜 화면으로 넘겨줘야 한다.
C. 화면에서 `GetBlockEvent()` 시스템 함수를 사용하여 안쪽 블록의 데이터를 직접 가져온다.
D. 블록 간 이벤트 전달은 불가능하므로 Client Variable을 사용하여 데이터를 공유해야 한다.

**문제 2. `On Render` 이벤트 내에서 화면의 로컬 변수 값을 변경하고 있습니다. 이 경우 발생할 수 있는 가장 심각한 문제는?**
A. 보안 취약점이 발생하여 외부 해킹에 노출된다.
B. 무한 루프(Infinite Loop)에 빠져 브라우저가 응답하지 않게 된다.
C. 해당 변수와 연결된 Database의 데이터가 자동으로 수정된다.
D. `On Initialize` 이벤트가 다시 실행되어 초기 데이터가 손실된다.

**문제 3. 화면 로드 시 `Aggregate A`는 `At Start`이고, `Data Action B`는 `Only on Demand`입니다. `On Ready` 이벤트에서 `B`를 호출하는 로직이 있다면, 실제 실행 순서는?**
A. Aggregate A 완료 -> On Ready 실행 -> Data Action B 실행
B. Aggregate A와 Data Action B가 동시에 비동기로 실행
C. Data Action B 완료 -> Aggregate A 실행 -> On Ready 실행
D. On Ready 실행 -> Aggregate A와 Data Action B가 순차적으로 실행

---

### **[Part 2. Logic & Validation (심화)]**

**문제 04. 버튼의 `Built-in Validation`이 `True`인 폼에서, 사용자가 필수 필드를 비워두고 버튼을 눌렀습니다. 이때 Client Action 내의 `If Form.Valid` 노드를 체크하지 않고 바로 Server Action을 호출하면 어떻게 됩니까?**
A. 플랫폼이 서버 호출 단계에서 자동으로 에러를 발생시키고 로직을 중단한다.
B. 화면에는 에러 메시지가 표시되지만, 로직은 빈 값을 가지고 Server Action을 그대로 실행한다.
C. 서버 액션이 실행되기 직전에 브라우저가 자동으로 새로고침되어 입력값이 초기화된다.
D. `Form.Valid`가 `False`이면 버튼에 연결된 Client Action 자체가 아예 실행되지 않는다.

**문제 05. `Server Action A`에서 예외가 발생하여 `Exception Handler`로 넘어갔습니다. 해당 핸들러의 `Abort Transaction` 속성이 `No`로 설정되어 있다면, 이 액션을 호출한 Client Action의 결과는?**
A. Server Action 내의 데이터 변경사항이 유지된 채로 Client Action의 다음 로직이 실행된다.
B. 모든 데이터 변경사항이 롤백되고 Client Action의 전역 예외 처리기로 이동한다.
C. 서버와의 연결이 즉시 끊어지고 사용자 세션이 종료된다.
D. `Abort Transaction`이 `No`이면 예외가 무시되어 에러 로그가 남지 않는다.

**문제 06. Client Action에서 `ListFilter`를 사용하여 1,000개의 레코드 중 10개를 추출했습니다. 추출된 10개 중 첫 번째 레코드의 값을 수정하면 원본 리스트(1,000개)의 해당 데이터는 어떻게 됩니까?**
A. 원본 리스트는 영향을 받지 않고 필터링된 리스트의 값만 바뀐다.
B. 원본 리스트의 해당 레코드 값도 자동으로 변경된다 (Reference 참조).
C. `ListFilter` 결과는 읽기 전용이므로 값을 수정하는 순간 런타임 에러가 발생한다.
D. 원본 리스트가 자동으로 다시 필터링되어 결과 리스트가 초기화된다.

---

### **[Part 3. Data Fetching & Aggregates (심화)]**

**문제 07. `Aggregate`에서 `Entity A`와 `Entity B`를 `Only With`로 조인했습니다. 만약 `B` 엔티티에 필터를 걸었는데 결과가 0건이라면, 전체 Aggregate의 결과는?**
A. `Entity A`의 데이터는 모두 출력되고 `Entity B` 부분만 비어서 나온다.
B. 조인 방식에 상관없이 `Entity A`의 모든 데이터가 출력된다.
C. 아무런 레코드도 반환되지 않는다 (0건).
D. `Entity B`의 모든 레코드가 출력되고 `Entity A`가 필터링된다.

**문제 08. Screen Aggregate의 `Max Records`를 10으로 설정하고, `StartIndex`를 5로 설정했습니다. 실제 데이터베이스에 100건의 데이터가 있을 때, 이 Aggregate가 반환하는 리스트의 `Count` 값은?**
A. 100
B. 10
C. 5
D. 15

**문제 09. `Data Action` 내부에서 `Server Action`을 호출하여 데이터를 가공한 뒤 출력하고 있습니다. 이 `Data Action`의 `Fetch` 속성이 `At Start`일 때, 화면 성능에 미치는 영향은?**
A. 서버에서 모든 처리가 끝나야 화면 렌더링이 시작되므로 초기 로딩 속도가 느려질 수 있다.
B. 비동기로 실행되므로 화면 렌더링에는 전혀 지장을 주지 않는다.
C. `Data Action`은 클라이언트에서만 실행되므로 서버 성능에 영향을 주지 않는다.
D. 화면의 다른 `Aggregate` 실행이 모두 끝난 후에야 `Data Action`이 시작된다.

---

### **[Part 4. Data Modelling & Relationships (심화)]**

**문제 10. `User` 엔티티와 `Profile` 엔티티가 1:1 관계입니다. `Profile` 엔티티의 ID가 `User Identifier` 타입일 때, `Profile` 레코드를 삭제하려고 하면 발생하는 현상은? (Delete Rule은 Protect)**
A. `User` 레코드가 존재하므로 `Profile` 레코드를 삭제할 수 없다.
B. `Profile` 레코드는 `User` 레코드의 존재 여부와 상관없이 삭제 가능하다.
C. `Profile`을 삭제하면 참조하고 있는 `User` 레코드도 함께 삭제된다.
D. 1:1 관계에서는 삭제가 불가능하며 `IsActive` 플래그를 써야만 한다.

**문제 11. `Static Entity`의 `Is_Active` 속성을 `False`로 변경하고 배포했습니다. 기존에 이 데이터를 참조하고 있던 일반 엔티티의 레코드들은 어떻게 됩니까?**
A. 참조 무결성 에러가 발생하여 해당 레코드들을 읽을 수 없게 된다.
B. 데이터는 그대로 유지되지만, 런타임에 Aggregate 필터 등에서 제외될 수 있다.
C. 데이터베이스에서 해당 레코드들이 자동으로 삭제된다.
D. 해당 `Static Entity`를 참조하는 모든 외래 키 값이 `Null`로 변경된다.

---

### **[Part 5. Architecture & Security (심화)]**

**문제 12. `Producer` 모듈에서 `Entity A`의 `Expose Read Only`를 `Yes`로 설정했습니다. `Consumer` 모듈에서 이 엔티티의 데이터를 수정하기 위해 가장 올바른 아키텍처는?**
A. `Consumer` 모듈에서 `SQL` 위젯을 사용하여 직접 `UPDATE` 문을 작성한다.
B. `Producer` 모듈에서 데이터를 수정하는 `Public Server Action`을 만들어 제공한다.
C. `Consumer` 모듈에서 `Entity A`를 복제하여 새로운 엔티티를 만든다.
D. `Expose Read Only` 설정과 상관없이 `CreateEntity` 액션을 강제로 호출한다.

**문제 13. 한 화면에 `Anonymous`와 `Registered` 역할이 모두 체크되어 있습니다. 이 화면에 대한 접근 제어 설명으로 옳은 것은?**
A. 로그인 여부와 상관없이 누구나 접근할 수 있다.
B. 반드시 로그인한 사용자만 접근할 수 있다 (Registered 우선).
C. 로그인을 하면 `Registered`로, 안 하면 `Anonymous`로 인식되어 접근 가능하다.
D. 두 역할이 동시에 체크되면 충돌이 발생하여 아무도 접근할 수 없다.

---

### **[Part 6. 복합 시나리오 퀴즈 (7문항)]**

**문제 14. 클라이언트 변수(Client Variable)에 현재 페이지의 검색 필터 조건을 저장했습니다. 사용자가 브라우저 탭을 복제(Duplicate)하여 새 탭을 열었을 때, 새 탭의 검색 조건은 어떻게 됩니까?**
A. 새 탭은 별도의 세션을 가지므로 검색 조건이 초기화되어 있다.
B. 기존 탭과 동일한 검색 조건을 공유한다.
C. 새 탭에서는 보안을 위해 클라이언트 변수를 읽을 수 없다.
D. 서버에서 다시 데이터를 받아올 때까지 값이 보이지 않는다.

**문제 15. `Aggregate`의 `Join` 조건에서 `With or Without`을 사용하고, `Filter` 탭에서 오른쪽 엔티티의 특정 속성이 `Null`인 데이터만 찾도록 설정했습니다. 이 로직의 실제 의도는?**
A. 양쪽 엔티티에 모두 데이터가 있는 것만 찾기 위함이다.
B. 왼쪽 엔티티에는 데이터가 있지만, 오른쪽 엔티티에는 매칭되는 데이터가 **없는** 것들만 찾기 위함이다 (Left Anti Join).
C. 오른쪽 엔티티의 모든 데이터를 가져오기 위함이다.
D. `Null` 값은 필터링할 수 없으므로 런타임 에러가 발생한다.

**문제 16. `Pagination` 위젯을 사용하여 리스트를 구현했습니다. `StartIndex`를 20으로 변경하고 `Refresh Data`를 수행했을 때, 서버에서 가져오는 레코드의 범위는? (MaxRecords = 10)**
A. 1번부터 30번까지의 레코드
B. 21번부터 30번까지의 레코드
C. 20번부터 100번까지의 모든 레코드
D. 1번부터 10번까지의 레코드만 다시 가져온다.

**문제 17. `On Initialize` 이벤트에서 `JavaScript` 노드를 사용하여 화면 위젯의 `Id`를 참조하려고 합니다. 결과는?**
A. 위젯의 `Id`를 정상적으로 가져와서 조작할 수 있다.
B. 화면이 아직 렌더링되지 않았으므로 위젯의 `Id`는 `Undefined`이거나 에러가 발생한다.
C. `On Initialize`에서는 자바스크립트를 아예 사용할 수 없다.
D. 시스템이 자동으로 `On Ready`가 끝날 때까지 자바스크립트 실행을 지연시킨다.

**문제 18. `Binary Data` 타입의 대용량 이미지를 `Client Variable`에 저장하려고 시도할 때 발생하는 현상은?**
A. 이미지가 자동으로 압축되어 저장된다.
B. 저장 속도가 매우 느려지지만 정상적으로 저장된다.
C. `Client Variable`은 `Binary Data` 타입을 지원하지 않으므로 디자인 타임 에러가 발생한다.
D. 앱이 실행될 때 메모리 부족 에러로 강제 종료된다.

**문제 19. 화면의 `On Destroy` 이벤트가 실행되는 시점은?**
A. 사용자가 화면 내의 '삭제' 버튼을 눌렀을 때
B. 다른 화면으로 이동하기 위해 현재 화면이 소멸되기 직전
C. 브라우저 창이 최소화되었을 때
D. 서버와의 연결이 끊어져서 세션이 종료되었을 때

**문제 20. `Dropdown` 위젯의 `Source Entity`가 `Static Entity`입니다. `Mandatory` 속성이 `No`일 때, 사용자가 아무것도 선택하지 않으면 변수에는 어떤 값이 담깁니까?**
A. `Null` 문자열
B. 해당 `Static Entity`의 첫 번째 레코드 ID
C. `NullIdentifier()` (기본값)
D. 에러가 발생하여 로직이 중단됨

---

**상당히 까다로운 문제들이 섞여 있습니다. SI 실무에서 흔히 발생하는 '함정'들을 떠올리며 풀어보세요. 답안을 주시면 1번부터 아주 상세하게, "왜 헷갈리는지"와 "정답인 이유"를 풀이해 드리겠습니다!**