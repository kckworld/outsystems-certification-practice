번호,정답,번호,정답,번호,정답,번호,정답,번호,정답
01,B,06,B,11,A,16,C,21,B
02,C,07,B,12,B,17,C,22,D
03,A,08,D,13,B,18,B,23,B
04,B,09,C,14,B,19,B,24,B
05,A,10,A,15,B,20,B,25,B

번호,정답,번호,정답,번호,정답,번호,정답,번호,정답
26,B,31,B,36,A,41,A,46,B
27,B,32,C,37,A,42,B,47,B
28,A,33,C,38,B,43,A,48,B
29,B,34,A,39,A,44,B,49,B
30,A,35,B,40,A,45,A,50,B

번호,정답,번호,정답,번호,정답,번호,정답,번호,정답
51,B,56,A,61,B,66,D,71,B
52,B,57,A,62,B,67,A,72,B
53,B,58,C,63,B,68,B,73,B
54,B,59,B,64,B,69,B,74,B
55,B,60,B,65,B,70,B,75,B

번호,정답,번호,정답,번호,정답,번호,정답,번호,정답
76,B,81,D,86,A,91,A,96,A
77,A,82,A,87,A,92,B,97,A
78,A,83,B,88,A,93,A,98,A
79,B,84,B,89,B,94,C,99,B
80,B,85,A,90,A,95,A,100,B

### **[UI 디자인 & 위젯]**

**01. Screen에 대량의 데이터를 표시하는 Table 위젯이 있습니다. 특정 열(Column)의 너비를 고정하거나 스타일을 입히기 위해 가장 권장되는 방법은?**
A. Table 위젯 전체의 속성에서 Inline Style을 작성한다.
B. 해당 열의 Header 또는 Row Cell 내부의 Container/Widget 스타일을 수정한다.
C. CSS 컴파일러를 통해 Table의 모든 태그를 강제로 덮어쓴다.
D. Table 위젯은 스타일 수정이 불가능하므로 HTML 위젯을 직접 짠다.

**02. 부모 화면에서 Web Block의 Input Parameter 값을 변경했습니다. 이때 해당 Block 내부에서 특정 로직을 즉시 실행하고 싶다면 어떤 이벤트를 써야 하는가?**
A. On Initialize
B. On Ready
C. On Parameters Changed
D. On Render

**03. Form 위젯 내부에 'Save' 버튼이 있습니다. 사용자가 필수 항목을 입력하지 않았을 때, 버튼 옆에 "모든 필드를 입력하세요"라는 메시지를 띄우고 싶다면?**
A. 버튼의 Validation Message 속성을 수정한다.
B. Form 위젯의 Validation Parent 속성을 활용한다.
C. `If` 위젯을 사용하여 `Form.Valid`가 False일 때 메시지가 보이도록 한다.
D. JavaScript의 `alert()` 창을 띄운다.

**04. 이미지 위젯(Image Widget)에서 외부 URL의 이미지를 보여주려 할 때, `Type` 속성의 설정값은?**
A. Local
B. External
C. Database
D. Binary

**05. Web Block이 화면에서 사라질 때(예: 화면 이동) 클라이언트 측 리소스를 정리하거나 로그를 남기고 싶다면 사용하는 이벤트는?**
A. On Destroy
B. On Render
C. On Parameters Changed
D. On Initialize

### **[로직 & 액션]**

**06. Client Action에서 Server Action을 호출했습니다. 서버에서 에러가 발생해 Exception이 던져졌을 때, Client Action의 흐름은 어떻게 되는가?**
A. 에러를 무시하고 다음 노드를 계속 실행한다.
B. 즉시 실행을 멈추고 해당 Client Action의 Exception Handler(또는 전역 핸들러)로 이동한다.
C. 서버에서 자동으로 재시도를 3번 수행한다.
D. 사용자의 브라우저 세션이 즉시 종료된다.

**07. 여러 개의 서버 액션을 호출하는 로직이 있습니다. 이들을 하나의 서버 액션(Wrapper)으로 묶어서 호출할 때 얻는 가장 큰 이득은?**
A. 보안이 강화된다.
B. 네트워크 통신(Round-trip) 횟수가 줄어들어 성능이 향상된다.
C. 데이터베이스 용량이 절약된다.
D. 클라이언트 변수를 더 많이 사용할 수 있다.

**08. `ListAppend` 시스템 액션을 사용하여 리스트에 아이템을 추가했습니다. 이 변경사항은 언제 데이터베이스에 반영되는가?**
A. 추가되는 즉시 자동으로 반영된다.
B. `ListAppend` 실행 후 `UpdateEntity` 액션을 추가로 호출해야 반영된다.
C. `CommitTransaction` 노드를 지나야 반영된다.
D. `ListAppend`는 메모리 내 작업이므로 DB와는 상관이 없다.

**09. `Switch` 노드를 사용하여 4개의 경로를 만들었습니다. 모든 조건이 False일 때 실행되는 경로는?**
A. 첫 번째 경로
B. 가장 마지막에 추가된 경로
C. "Otherwise"로 지정된 경로
D. 런타임 에러가 발생한다.

**10. Client Action 내에서 JavaScript 노드를 사용하고 있습니다. 자바스크립트 내의 값을 다시 OutSystems 액션의 변수로 가져오려면?**
A. JavaScript 노드의 Output Parameter를 정의하고 값을 할당한다.
B. 전역 변수(window.variable)를 사용한다.
C. `JSON.stringify`를 사용하여 브라우저 쿠키에 저장한다.
D. JavaScript 노드에서는 값을 밖으로 내보낼 수 없다.

### **[데이터 페칭]**

**11. Aggregate에서 `Employee` 엔티티와 `Department` 엔티티를 `Only With`로 조인했습니다. 만약 부서(Department)가 배정되지 않은 직원을 찾고 싶다면 어떤 조인으로 바꿔야 하는가?**
A. With or Without
B. Full Outer Join
C. Not With
D. Cross Join

**12. 화면 로드 시 데이터를 가져오는 Aggregate의 `Fetch` 속성이 `At Start`입니다. 이 데이터가 도착하기 전에 화면의 위젯이 그려지면 어떤 현상이 발생하는가?**
A. 화면이 로딩되지 않고 에러가 발생한다.
B. 데이터가 비어있는 상태로 위젯이 먼저 그려지고, 데이터 도착 시 자동으로 업데이트된다.
C. 데이터가 올 때까지 브라우저 화면 자체가 하얗게 멈춘다.
D. `On Initialize`가 두 번 실행된다.

**13. Aggregate의 `Sorting` 탭에서 고정된 정렬이 아닌, 사용자가 클릭한 컬럼에 따라 정렬을 바꾸고 싶다면?**
A. 각 컬럼마다 별도의 Aggregate를 만든다.
B. Dynamic Sort 기능을 사용하여 변수를 전달한다.
C. `ListSort` 시스템 액션을 클라이언트 단에서 매번 실행한다.
D. 정렬은 Aggregate에서 변경할 수 없다.

**14. Data Action 내부에서 여러 개의 엔티티를 조회하고 복잡한 계산을 수행한 뒤 3개의 Output 파라미터를 반환했습니다. 이 Data Action은 화면에서 언제 실행되는가?**
A. Aggregate가 모두 끝난 후에 실행된다.
B. Screen Aggregate들과 함께 비동기로 동시에 실행된다.
C. `On Ready` 이벤트가 끝난 후에 실행된다.
D. 사용자가 화면을 스크롤할 때 실행된다.

**15. Aggregate의 `Max Records` 속성에 50을 입력했습니다. 결과가 100건이라면 `List.Count`와 `List.Length` 중 50을 반환하는 것은?**
A. List.Count
B. List.Length
C. 둘 다 50을 반환한다.
D. 둘 다 100을 반환한다.

### **[데이터 모델링]**

**16. 일반 Entity를 생성하고 Primary Key인 ID의 데이터 타입을 `Text`로 바꿨습니다. 이때 잃게 되는 기능은?**
A. 데이터를 삭제하는 기능
B. 인덱스를 추가하는 기능
C. Is Autonumber (자동 번호 생성) 기능
D. 외래 키로 참조되는 기능

**17. `Delete Rule`이 `Delete (Cascade)`인 관계에서 부모 레코드를 삭제했습니다. 자식 레코드들은 어떻게 되는가?**
A. 그대로 유지되며 외래 키만 비워진다.
B. 삭제되지 않고 에러가 발생한다.
C. 부모 레코드와 함께 자동으로 삭제된다.
D. 백업 테이블로 자동으로 이동한다.

**18. Static Entity의 레코드 중 하나를 더 이상 사용하지 않아 삭제하고 싶지만, 이미 많은 데이터가 참조 중입니다. 가장 좋은 방법은?**
A. 강제로 삭제하고 DB 에러를 무시한다.
B. `Is_Active` 속성을 `False`로 설정하여 더 이상 선택되지 않게 한다.
C. 참조 중인 모든 데이터를 먼저 지우고 삭제한다.
D. 일반 Entity로 변환한다.

### **[라이프사이클 & 아키텍처 & 보안]**

**19. 화면의 `On Render` 이벤트에 대한 설명으로 옳은 것은?**
A. 화면이 처음 로드될 때 딱 한 번만 실행된다.
B. 화면 내 데이터가 변경되어 UI가 갱신될 때마다 실행된다.
C. 서버 액션이 실행될 때마다 호출된다.
D. `On Initialize`보다 먼저 실행된다.

**20. Client Variable에 저장된 값은 언제 초기화되는가?**
A. 브라우저 탭을 닫을 때
B. 사용자가 로그아웃하거나 로직으로 값을 지울 때
C. 서버가 재시작될 때
D. 24시간이 지나면 자동으로 초기화된다.

**21. `CheckRegisteredRole()` 함수가 `False`를 반환했다면, 현재 사용자의 상태는?**
A. 관리자 계정이다.
B. 로그인하지 않은 익명(Anonymous) 사용자이다.
C. 비밀번호가 만료된 사용자이다.
D. 차단된 IP에서 접속한 사용자이다.

**22. Producer 모듈에서 `Public` 서버 액션의 로직을 수정하고 배포했습니다. Consumer 모듈을 다시 배포(Publish)하지 않아도 최신 로직이 적용되는 이유는?**
A. 서버 액션은 런타임에 동적으로 참조되기 때문이다.
B. OutSystems가 자동으로 모든 모듈을 재배포하기 때문이다.
C. 서버 액션은 클라이언트 변수에 저장되기 때문이다.
D. 인터페이스가 바뀌지 않았기 때문이다.

**23. 화면의 `Roles` 설정에서 `Anonymous`를 체크 해제하고 `Registered`만 체크했습니다. 로그인하지 않은 사용자가 URL로 직접 접근하면?**
A. 빈 화면이 뜬다.
B. 로그인 화면으로 리다이렉트되거나 접근 거부 에러가 뜬다.
C. 임시 권한으로 화면을 볼 수 있다.
D. 브라우저가 강제로 종료된다.

**24. Client Variable을 남용할 경우 발생할 수 있는 주요 문제는?**
A. 서버 메모리 부족
B. 브라우저 성능 저하 및 보안 취약점 노출
C. 데이터베이스 커넥션 풀 부족
D. CSS 스타일 충돌

**25. `Pagination` 위젯의 `StartIndex` 변수를 0에서 10으로 바꿨습니다. 화면의 리스트를 갱신하기 위해 반드시 호출해야 하는 노드는?**
A. Destination
B. Refresh Data (해당 Aggregate 선택)
C. On Render
D. JavaScript



**[UI 디자인 & 위젯]**
**26. `Container` 위젯의 `Visible` 속성에 `False`를 설정했을 때 나타나는 현상은?**
A. 화면에서 보이지 않지만 HTML DOM에는 존재한다.
B. 화면에서 사라지고 HTML DOM에서도 완전히 제거된다.
C. 투명도만 0%가 되어 자리는 차지하고 있다.
D. 서버에서 데이터를 아예 가져오지 않는다.

**27. 화면에 배치된 `Form` 위젯의 `Name` 속성을 지정해야 하는 가장 큰 이유는?**
A. CSS 스타일을 적용하기 위해
B. 로직(Client Action)에서 `Form1.Valid` 처럼 폼의 상태를 참조하기 위해
C. 데이터베이스 테이블 이름과 맞추기 위해
D. 다국어 지원을 위해

**28. `List` 위젯 내부에 `If` 위젯을 사용하여 특정 조건일 때만 아이템을 보여주고 있습니다. 조건이 `False`인 아이템들이 리스트의 `Length`에 포함됩니까?**
A. 포함된다. (UI에서만 안 보일 뿐 리스트 데이터에는 존재함)
B. 포함되지 않는다.
C. `Refresh Data`를 해야만 제외된다.
D. `Empty Message`가 출력된다.

**29. `Link` 위젯의 `Transition` 속성을 설정하여 화면 전환 효과를 줄 수 있는 `Type`은?**
A. External URL
B. Screen (현재 앱 내 화면)
C. Mailto
D. JavaScript

**30. Web Block에서 이벤트를 정의할 때, `Input Parameter`를 이벤트의 데이터로 실어 보낼 수 있습니까?**
A. 예, 가능합니다.
B. 아니요, 이벤트는 신호만 보낼 수 있습니다.
C. 오직 Text 타입만 가능합니다.
D. 부모 화면이 허용할 때만 가능합니다.

**[로직 & 액션]**
**31. `Server Action`에서 예외(Exception)를 발생시키기 위해 `Raise Exception` 노드를 사용했습니다. 이 액션에 `Exception Handler`가 정의되어 있지 않다면?**
A. 에러가 무시되고 다음 로직이 실행된다.
B. 이 액션을 호출한 상위 액션(Client Action 등)의 예외 처리기로 전파된다.
C. 서버가 즉시 재시작된다.
D. 변수값들이 초기화되고 로직이 처음부터 다시 실행된다.

**32. `Assign` 노드에서 하나의 변수에 여러 번 값을 할당하면 최종적으로 어떤 값이 남습니까?**
A. 첫 번째 할당된 값
B. 모든 값의 합계
C. 가장 마지막(아래쪽)에 할당된 값
D. 에러가 발생한다.

**33. `Client Action` 내에서 `Destination` 노드를 사용하여 다른 화면으로 이동하도록 설정했습니다. 이 노드 이후에 배치된 다른 로직들은 어떻게 됩니까?**
A. 화면 이동과 동시에 실행된다.
B. 화면 이동이 완료된 후 실행된다.
C. 실행되지 않는다. (Destination은 액션의 종료점 역할)
D. 백그라운드에서 실행된다.

**34. 사용자가 입력한 데이터의 유효성을 서버 단에서도 다시 한번 검사(Server-side Validation)해야 하는 주요 이유는?**
A. 클라이언트 측 검사는 우회될 가능성이 있어 데이터 무결성을 보장하기 위해
B. 서버 액션이 더 빠르기 때문
C. `Form.Valid` 속성을 서버에서만 읽을 수 있기 때문
D. 디자인 가이드라인이기 때문

**35. `User_Logout` 시스템 액션을 실행하면 발생하는 현상은?**
A. 현재 사용자의 브라우저 쿠키만 지운다.
B. 서버 세션을 종료하고 사용자를 익명(Anonymous) 상태로 만든다.
C. 사용자의 아이디를 데이터베이스에서 삭제한다.
D. 모든 클라이언트 변수를 즉시 초기화한다.

**[데이터 페칭]**
**36. `Aggregate`에서 `Join` 조건으로 사용되는 속성을 변경했습니다. 이에 따라 자동으로 업데이트되는 것은?**
A. 결과 리스트의 데이터 구조 (Data Type)
B. 데이터베이스의 실제 테이블 관계
C. 화면의 모든 로컬 변수
D. 사용자의 로그인 세션

**37. `Aggregate`의 `Filter` 조건에 `Employee.IsActive = True`를 추가했습니다. 결과에 미치는 영향은?**
A. 활성화된 직원만 결과 리스트에 포함된다.
B. 모든 직원을 가져온 뒤 화면에서 필터링한다.
C. 활성화되지 않은 직원은 `Deleted` 상태로 표시된다.
D. `IsActive` 컬럼이 결과에서 사라진다.

**38. `Only on demand`로 설정된 `Data Action`을 로직에서 수동으로 실행하고 싶을 때 사용하는 노드는?**
A. Refresh Data
B. Run Data Action
C. Assign
D. JavaScript

**39. `Aggregate`의 결과값 중 첫 번째 레코드의 특정 값을 가져오기 위한 올바른 접근 경로는?**
A. `GetEmployees.List.Current.Employee.Name`
B. `GetEmployees.First.Name`
C. `GetEmployees.Employee.Name`
D. `GetEmployees.List[0].Name`

**40. `Data Action` 내부에서 `Database Entity`를 조회하는 `Aggregate`를 여러 개 넣을 수 있습니까?**
A. 예, 가능합니다.
B. 아니요, Data Action당 하나만 가능합니다.
C. 오직 서버 액션을 통해서만 가능합니다.
D. `Fetch` 속성이 `At Start`일 때만 가능합니다.

**[데이터 모델링]**
**41. `Entity`의 속성 중 `Mandatory`를 `Yes`로 설정했을 때 데이터베이스 레벨에서 발생하는 변화는?**
A. 해당 컬럼에 `NOT NULL` 제약 조건이 추가된다.
B. 해당 컬럼이 인덱스로 설정된다.
C. 중복 입력을 허용하지 않는다.
D. 데이터 타입이 자동으로 `Text`가 된다.

**42. `Static Entity`의 `Order` 속성의 역할은 무엇입니까?**
A. 데이터가 데이터베이스에 저장되는 물리적 순서
B. 드롭다운 등 UI에서 레코드가 표시되는 기본 정렬 순서
C. 결제 시스템에서의 주문 번호
D. 참조되는 횟수

**43. `Delete Rule`이 `Ignore`인 경우, 부모 레코드를 삭제하면 어떤 위험이 있습니까?**
A. 자식 레코드가 존재하지 않는 부모를 가리키게 되어 데이터 무결성이 깨진다.
B. 모든 데이터가 한꺼번에 삭제된다.
C. 서버 성능이 급격히 저하된다.
D. 삭제된 데이터가 자동으로 복구된다.

**44. `Entity A`에 `Entity B Identifier` 타입의 속성을 추가했습니다. 생성된 관계의 종류는?**
A. 1:1
B. 1:N
C. N:M
D. 관계가 형성되지 않는다.

**[리액티브 앱 & 라이프사이클]**
**45. `On Parameters Changed` 이벤트 핸들러 내에서 `Refresh Data`를 수행하는 주된 이유는?**
A. 부모로부터 받은 새로운 입력값에 맞춰 데이터를 다시 조회하기 위해
B. 화면 전체를 새로고침하기 위해
C. 클라이언트 변수를 서버로 전송하기 위해
D. 사용자를 로그아웃시키기 위해

**46. `On Initialize` 이벤트가 실행되는 시점에 화면의 위젯들이 브라우저에 렌더링되어 있습니까?**
A. 예, 이미 렌더링이 완료된 상태입니다.
B. 아니요, 아직 렌더링 전입니다.
C. `At Start` 데이터가 도착한 경우에만 렌더링됩니다.
D. 오직 모바일 기기에서만 렌더링됩니다.

**47. `Client Variable`의 값을 변경하면 이를 사용 중인 모든 화면의 UI가 자동으로 갱신됩니까?**
A. 예, 즉시 갱신됩니다.
B. 아니요, 화면을 새로고침하거나 로직으로 다시 읽어야 합니다.
C. `On Render`가 실행될 때만 갱신됩니다.
D. 서버와의 동기화가 끝난 후에 갱신됩니다.

**48. `On Ready` 이벤트는 주로 어떤 작업을 할 때 사용합니까?**
A. 서버에서 초기 데이터를 가져올 때
B. 자바스크립트를 사용하여 특정 위젯에 포커스를 주거나 외부 라이브러리를 초기화할 때
C. 사용자의 권한을 서버에서 확인할 때
D. 데이터베이스 테이블을 생성할 때

**[아키텍처 & 보안]**
**49. `Producer` 모듈에서 `Public` 서버 액션을 삭제했을 때, 이를 참조하던 `Consumer` 모듈에서 발생하는 현상은?**
A. 실행 시점에만 에러가 난다.
B. 디자인 타임(Service Studio)에서 즉시 'Missing Dependency' 에러가 발생한다.
C. 삭제된 액션이 자동으로 빈 액션으로 대체된다.
D. 아무런 영향을 주지 않는다.

**50. `CheckManagerRole(GetUserId())` 함수의 반환값이 `True`라면, 이 사용자는 어떤 권한을 가지고 있는 것입니까?**
A. 모든 화면에 접근 가능한 Admin 권한
B. 'Manager'라는 이름으로 정의된 특정 Role 권한
C. 서버의 모든 파일을 읽을 수 있는 권한
D. 다른 사용자의 비밀번호를 바꿀 수 있는 권한



**[UI 디자인 & 위젯]**
**51. `If` 위젯의 `True` 영역에 배치된 위젯들이 화면에 보이지 않는 조건은?**
A. `Condition` 속성이 `True`일 때
B. `Condition` 속성이 `False`일 때
C. `Visible` 속성이 `Always`일 때
D. `Data Action`이 실행 중일 때

**52. 여러 개의 위젯을 논리적으로 그룹화하고, 한꺼번에 스타일이나 레이아웃을 적용하기 위해 사용하는 가장 기본적인 위젯은?**
A. Placeholder
B. Container
C. Expression
D. Button Group

**53. `Form` 위젯 내부의 `Input` 위젯을 우클릭하여 'Valid' 속성을 수동으로 바꿀 수 있는 위치는?**
A. 위젯의 Properties 패널
B. 오직 Client Action 내의 Assign 노드
C. Service Center
D. 데이터베이스 엔티티 속성

**54. `Menu` 위젯이 모든 화면에서 동일하게 나타나도록 구성할 때, 가장 적절한 구현 방식은?**
A. 각 화면마다 메뉴를 직접 그린다.
B. 메뉴를 `Web Block`으로 만들고 각 화면의 레이아웃에 포함시킨다.
C. `Site Property`에 메뉴 코드를 넣는다.
D. `Client Variable`을 사용하여 메뉴를 생성한다.

**55. `Web Block`의 `Input Parameter`에 전달된 값이 바뀌었을 때, 특정 Aggregate를 갱신하지 않으면 발생하는 현상은?**
A. 화면에 에러가 발생한다.
B. 화면에 이전 데이터(Old Data)가 그대로 유지된다.
C. 사용자가 자동으로 로그아웃된다.
D. 브라우저가 강제로 새로고침된다.

**[로직 & 액션]**
**56. `Exception Handler` 노드에서 `All Exceptions`를 처리하도록 설정했을 때의 장점은?**
A. 특정 에러뿐만 아니라 예상치 못한 모든 런타임 에러를 한곳에서 잡을 수 있다.
B. 에러가 발생해도 프로그램이 중단되지 않고 계속 실행된다.
C. 에러 로그가 DB에 저장되지 않아 성능이 빨라진다.
D. 사용자에게 에러 메시지를 보여주지 않는다.

**57. `Client Action` 내에서 `Server Action`을 호출하는 흐름 사이에 `JavaScript` 노드를 넣어 데이터를 가공하는 것이 가능합니까?**
A. 예, 가능합니다.
B. 아니요, 자바스크립트는 액션 끝에만 넣을 수 있습니다.
C. 오직 오프라인 앱에서만 가능합니다.
D. 서버 액션 내부에서만 자바스크립트를 쓸 수 있습니다.

**58. `For Each` 루프 내부에서 `Break`와 같은 역할을 수행하여 반복문을 강제로 빠져나가려면?**
A. `End` 노드를 사용한다.
B. `Assign` 노드를 사용하여 인덱스를 최대값으로 바꾼다.
C. 루프의 다음 노드를 반복문 밖의 노드로 연결한다.
D. `Raise Exception`을 사용한다.

**59. `Validation` 로직 수행 중, `Form.Valid`를 `False`로 설정하고 `End` 노드로 액션을 끝냈을 때 UI에 나타나는 현상은?**
A. 아무런 변화가 없다.
B. 유효하지 않은 위젯 옆에 설정된 `Validation Message`가 나타난다.
C. 화면이 즉시 이전 페이지로 이동한다.
D. 팝업창이 뜨며 경고를 보낸다.

**60. `Raise Exception` 노드로 발생시킨 에러를 잡기 위해 `Exception Handler`를 배치했습니다. 에러 발생 시 핸들러 이후의 원래 로직은 어떻게 됩니까?**
A. 계속해서 다음 노드가 실행된다.
B. 실행이 중단되고 핸들러 내부 로직만 실행된 후 끝난다.
C. 핸들러 실행 후 다시 원래 에러 발생 지점으로 돌아간다.
D. 화면이 자동으로 새로고침된다.

**[데이터 페칭]**
**61. `Aggregate`에서 `Join` 조건으로 사용되는 두 속성의 데이터 타입이 다를 경우 발생하는 현상은?**
A. 자동으로 타입이 변환되어 조인된다.
B. 디자인 타임(Service Studio)에서 에러 또는 경고가 발생한다.
C. 런타임에 성능이 2배로 빨라진다.
D. 조인 결과가 무조건 0건이 된다.

**62. `Screen Aggregate`의 `On After Fetch` 이벤트 핸들러 내에서 또 다른 `Refresh Data`를 호출할 때 가장 주의해야 할 점은?**
A. 보안 취약점
B. 무한 루프(Infinite Loop) 발생 가능성
C. 데이터베이스 용량 부족
D. 사용자 세션 만료

**63. `Data Action`이 실행되는 위치는 어디입니까?**
A. 사용자의 브라우저 (Client)
B. OutSystems 서버 (Server)
C. 데이터베이스 엔진 내부
D. 클라우드 스토리지

**64. `Aggregate`에서 특정 컬럼의 데이터를 기준으로 그룹화(`Group By`)를 수행하면 결과 리스트의 데이터 구조는 어떻게 됩니까?**
A. 원본 엔티티의 모든 속성을 유지한다.
B. 그룹화된 속성과 집계 함수(Sum, Count 등) 결과만 포함하도록 바뀐다.
C. 리스트가 아닌 단일 레코드로 바뀐다.
D. 데이터 구조는 변하지 않는다.

**65. `Fetch` 속성이 `Only on demand`인 Aggregate는 언제 데이터를 가져옵니까?**
A. 화면이 처음 열릴 때
B. 로직(Client Action)에서 명시적으로 `Refresh Data` 노드를 실행할 때
C. 사용자가 마우스를 위젯 위에 올릴 때
D. 5초마다 주기적으로

**[데이터 모델링]**
**66. `Entity`를 생성하면 자동으로 만들어지는 4가지 기본 액션(CRUD)이 아닌 것은?**
A. Create<Entity>
B. Update<Entity>
C. Delete<Entity>
D. Search<Entity>

**67. `Delete Rule`이 `Delete` (Cascade)인 관계는 주로 어떤 상황에서 사용합니까?**
A. 부모 데이터(예: 주문)를 지울 때 관련 상세 데이터(예: 주문상품들)도 함께 지워야 할 때
B. 데이터를 절대 지우고 싶지 않을 때
C. 보안이 중요한 데이터를 다룰 때
D. 다대다 관계를 만들 때

**68. `Static Entity`의 `Id` 데이터 타입을 `Text`로 설정했을 때 얻는 이점은?**
A. 데이터베이스 성능이 향상된다.
B. 코드 가독성이 좋아지며(예: "Active", "Inactive"), 하드코딩된 값과 비교하기 쉽다.
C. 더 많은 레코드를 저장할 수 있다.
D. 자동으로 숫자가 증가한다.

**[리액티브 앱 & 라이프사이클]**
**69. `On Destroy` 이벤트 내에서 수행하기 가장 적합한 작업은?**
A. 데이터베이스의 데이터를 대량으로 수정하는 작업
B. 현재 화면에서만 사용하던 자바스크립트 라이브러리나 타이머 해제
C. 다른 화면으로 데이터를 전송하는 작업
D. 사용자의 비밀번호 변경

**70. `Client Variable`에 저장된 정보가 모든 브라우저 탭에서 공유되는 이유는?**
A. 서버 메모리를 공유하기 때문
B. 브라우저의 동일한 로컬 저장소(Local Storage)를 사용하기 때문
C. OutSystems가 클라우드 기반이기 때문
D. 모든 탭이 동일한 CPU를 쓰기 때문

**71. `On Render` 이벤트가 `On Ready` 이벤트보다 먼저 발생할 수 있습니까?**
A. 예, 항상 먼저 발생합니다.
B. 아니요, `On Ready` 이후에 처음으로 `On Render`가 발생합니다.
C. 데이터가 없는 경우에만 먼저 발생합니다.
D. 모바일 앱에서만 가능합니다.

**[아키텍처 & 보안]**
**72. `Producer` 모듈에서 `Public`으로 설정된 엔티티의 `Expose Read Only`가 `No`일 때, Consumer 모듈이 할 수 있는 작업은?**
A. 데이터를 읽기만 할 수 있다.
B. 데이터를 읽고, 쓰고, 수정하고, 삭제하는 모든 CRUD 액션을 직접 사용할 수 있다.
C. 엔티티의 속성 이름을 직접 바꿀 수 있다.
D. 엔티티를 삭제할 수 있다.

**73. 두 모듈 간에 `Circular Dependency` (순환 참조)가 발생하면 생기는 주요 문제는?**
A. 앱의 아이콘이 바뀐다.
B. 모듈 간 결합도가 너무 높아져 유지보수와 배포가 매우 어려워진다.
C. 데이터베이스 용량이 두 배로 늘어난다.
D. 모든 사용자가 로그아웃된다.

**74. `Registered` 역할(Role)에 대한 설명으로 옳은 것은?**
A. 모든 방문자(로그인 여부 무관)를 포함한다.
B. 로그인에 성공하여 유효한 세션을 가진 모든 사용자를 포함한다.
C. 오직 관리자(IT Admin)만 포함한다.
D. 외부 API 호출자만 포함한다.

**75. `Producer` 모듈에서 액션의 '이름'을 변경하고 배포했습니다. Consumer 모듈에서 발생하는 현상은?**
A. 자동으로 이름이 바뀐다.
B. 'Incompatible Dependency' 에러가 발생하며 수동으로 업데이트(Refresh)해야 한다.
C. 이전 이름을 계속 사용할 수 있다.
D. Consumer 모듈이 자동으로 삭제된다.



**[UI 디자인 & 위젯]**
**76. `Dropdown` 위젯에서 `Empty Text` 속성의 역할은?**
A. 데이터가 없을 때 표시되는 에러 메시지
B. 사용자가 아무것도 선택하지 않았을 때(기본 상태) 표시되는 안내 문구 (예: "선택하세요")
C. 리스트의 마지막에 추가되는 텍스트
D. 데이터베이스의 Null 값을 대체하는 문자열

**77. `Form` 위젯 내부에서 버튼을 사용하지 않고 `Input` 위젯의 `On Change` 이벤트만으로 데이터를 저장하려고 합니다. 이때 `Form.Valid` 체크는 어떻게 해야 합니까?**
A. `On Change`에 연결된 Client Action 시작 부분에서 직접 체크해야 한다.
B. 버튼이 없으면 `Form.Valid`는 작동하지 않는다.
C. 플랫폼이 자동으로 저장 로직을 중단시킨다.
D. `On Change` 이벤트는 유효성 검사를 지원하지 않는다.

**78. 화면에 `List` 위젯이 있고, 각 아이템 안에 삭제 버튼이 있습니다. 버튼 클릭 시 해당 아이템의 데이터만 서버로 보내기 위해 필요한 것은?**
A. `List.Current` 값을 입력 파라미터로 받는 Client Action
B. 리스트 전체를 다시 조회하는 Data Action
C. 전체 리스트를 서버로 전송하는 로직
D. JavaScript를 통한 수동 데이터 추출

**[로직 & 액션]**
**79. `Client Action`에서 `Server Action`을 호출할 때 통신 오류(Network Error)가 발생했습니다. 이 에러를 잡기 위해 사용해야 하는 Exception Handler의 타입은?**
A. User Exception
B. Communication Exception
C. Database Exception
D. Security Exception

**80. `Switch` 노드에서 여러 조건이 동시에 `True`인 경우, 어떤 경로로 실행됩니까?**
A. 모든 True 경로가 동시에 실행된다.
B. 가장 먼저(위에서부터) True인 조건의 경로 하나만 실행된다.
C. 에러가 발생한다.
D. Otherwise 경로로 이동한다.

**81. `Assign` 노드를 사용하여 변수 A에 B 값을 넣고, 다시 B에 A 값을 넣었습니다. 결과적으로 B의 값은?**
A. 원래 B가 가지고 있던 값
B. 에러 발생
C. Null
D. 변수 A가 처음에 가지고 있던 값

**[데이터 페칭]**
**82. `Aggregate`에서 특정 엔티티를 `Source`에서 제거하면 발생하는 현상은?**
A. 해당 엔티티를 사용하던 모든 Filter와 Join 조건이 자동으로 삭제된다.
B. 데이터베이스에서 해당 테이블이 삭제된다.
C. 화면 전체가 에러로 인해 동작하지 않는다.
D. 해당 엔티티 데이터가 캐시에 저장된다.

**83. `Data Action`이 `At Start`로 설정되어 있을 때, 이 액션이 반환하는 Output Parameter를 화면 위젯에서 즉시 사용할 수 없는 시점은?**
A. `On After Fetch` 실행 전
B. `On Initialize` 실행 시점
C. `On Destroy` 실행 시점
D. `On Render` 실행 시점

**84. `Aggregate`의 `Sorting` 탭에 여러 개의 정렬 조건이 있을 때 우선순위는 어떻게 결정됩니까?**
A. 무작위로 결정된다.
B. 위에서 아래로 정의된 순서대로 적용된다.
C. 데이터 크기에 따라 결정된다.
D. 마지막에 정의된 조건만 적용된다.

**[데이터 모델링]**
**85. 엔티티의 `Index`를 생성할 때 여러 개의 속성(Attribute)을 묶어서 하나의 인덱스로 만들 수 있습니까?**
A. 예, 가능합니다 (복합 인덱스).
B. 아니요, 인덱스는 속성당 하나만 가능합니다.
C. 오직 Primary Key에만 가능합니다.
D. 정적 엔티티에서만 가능합니다.

**86. `User` 엔티티를 참조하는 `Foreign Key` 속성의 이름을 `CreatedBy`라고 지었습니다. 플랫폼은 이 관계를 어떻게 인식합니까?**
A. 이름과 상관없이 데이터 타입이 `User Identifier`이므로 `User` 엔티티와의 관계를 자동으로 형성한다.
B. 이름이 `UserId`가 아니므로 관계를 인식하지 못한다.
C. 반드시 수동으로 관계 설정을 연결해줘야 한다.
D. `CreatedBy`라는 이름은 시스템 예약어이므로 사용할 수 없다.

**87. `Static Entity`의 데이터를 수정한 후 배포(Publish)했습니다. 이 데이터 변경사항은 언제 반영됩니까?**
A. 배포 즉시 데이터베이스에 반영된다.
B. 사용자가 로그아웃해야 반영된다.
C. 서버를 재부팅해야 반영된다.
D. 1시간 뒤에 반영된다.

**[리액티브 앱 & 라이프사이클]**
**88. `Client Variable`은 동일한 브라우저의 다른 탭 간에 값을 공유합니까?**
A. 예, 공유합니다.
B. 아니요, 탭마다 독립적입니다.
C. 오직 시크릿 모드에서만 공유합니다.
D. 서버 설정을 통해서만 공유 가능합니다.

**89. `On Ready` 이벤트에서 자바스크립트를 사용해 위젯에 포커스를 주려고 합니다. 위젯의 `Id`를 얻기 위해 사용하는 올바른 속성은?**
A. Widget.Name
B. Widget.Id
C. Widget.RuntimeId
D. Widget.UniqueKey

**90. 화면 로컬 변수의 `Default Value`가 설정되어 있을 때, 이 값이 변수에 할당되는 시점은?**
A. `On Initialize` 직전
B. `On Ready` 직후
C. `On After Fetch` 완료 시
D. 데이터베이스 저장 시

**[아키텍처 & 보안]**
**91. `Producer` 모듈에서 서버 액션을 `Public = Yes`로 설정했지만, `Consumer` 모듈에서 보이지 않습니다. 이유는?**
A. `Consumer` 모듈에서 `Manage Dependencies`를 통해 참조를 추가하지 않았기 때문이다.
B. 서버 액션은 동일한 애플리케이션 내에서만 공유 가능하기 때문이다.
C. 사용자의 라이선스가 부족하기 때문이다.
D. `Producer` 모듈을 아직 Publish하지 않았기 때문이다.

**92. `Anonymous` 사용자에게 특정 버튼을 숨기고 싶을 때, 위젯의 `Visible` 속성에 넣을 가장 적절한 로직은?**
A. `GetUserId() <> NullIdentifier()`
B. `CheckRegisteredRole(GetUserId())`
C. 둘 다 정답이다.
D. `CheckAnonymousRole(GetUserId())`

**[복합/디버깅/기타]**
**93. 디버깅 중 특정 변수의 값을 실시간으로 모니터링하기 위해 사용하는 Service Studio의 창은?**
A. Debugger - Watch
B. Widget Tree
C. TrueChange
D. Service Center

**94. `Service Center`에서 확인할 수 없는 로그의 종류는?**
A. Error Logs
B. General Logs (LogMessage 액션 결과)
C. 개발자의 브라우저 히스토리
D. Extension Logs

**95. 외부 REST API를 `Expose` 할 때, 특정 HTTP 헤더를 필수값으로 받도록 설정할 수 있습니까?**
A. 예, Input Parameter를 추가하고 `Receive In` 속성을 `Header`로 설정하면 됩니다.
B. 아니요, 헤더는 시스템 전용입니다.
C. 오직 URL 파라미터만 가능합니다.
D. 자바스크립트를 써야만 가능합니다.

**96. `ListFilter`를 사용하여 필터링된 결과 리스트의 `Count`가 0일 때, `List.Current`를 참조하면 어떤 일이 발생합니까?**
A. 에러가 발생하지 않고 기본값(Empty Record)을 반환한다.
B. 즉시 런타임 에러가 발생한다.
C. 이전 리스트의 마지막 값을 반환한다.
D. 화면이 자동으로 새로고침된다.

**97. `Site Property`의 값을 `Service Center`에서 변경했습니다. 이 변경사항은 언제 앱에 반영됩니까?**
A. 변경 즉시 실시간으로 반영된다.
B. 다음번 Publish를 해야 반영된다.
C. 모든 사용자가 로그아웃해야 반영된다.
D. 매주 일요일에 일괄 반영된다.

**98. 화면에서 `Container`의 `Display` 속성을 `None`으로 설정하는 것과 `If` 위젯의 조건을 `False`로 하는 것의 결정적 차이는?**
A. `Display: None`은 HTML DOM에 존재하지만, `If: False`는 DOM에서 아예 생성되지 않는다.
B. 차이가 없다.
C. `If`는 서버 성능에 영향을 주지만 `Display`는 주지 않는다.
D. `Display`는 모바일에서만 작동한다.

**99. `Producer` 모듈에서 엔티티의 속성 '이름'을 바꿨습니다. Consumer 모듈을 수정하지 않고 Publish만 하면 어떻게 됩니까?**
A. 자동으로 이름이 바뀐 속성을 찾아 매핑한다.
B. `Broken Reference` 에러가 발생하며 컴파일이 되지 않는다.
C. 이전 속성 이름을 그대로 사용하여 실행된다.
D. 데이터가 모두 삭제된다.

**100. OutSystems 자격증 시험 합격을 위해 가장 중요한 마인드셋은? (보너스)**
A. 모든 내용을 달달 외운다.
B. 라이프사이클과 데이터 흐름의 인과관계를 이해한다.
C. 문제를 최대한 빨리 푼다.
D. 모르는 문제는 무조건 A를 찍는다.