# Certification - Associated Exam Questions

## Quick Answer Key
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ① | ④ | ① | ③ | ② | ③ | ① | ① | ① | ③ |

| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ③ | ③ | ③ | ③ | ③ | ④ | ③ | ① | ② | ③ |

| 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ④ | ③ | ② | ③ | ① | ③ | ② | ① | ③ | ① |

| 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ③ | ④ | ① | ② | ① | ② | ③ | ① | ② | ② |

| 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ③ | ③ | ① | ① | ② | ① | ③ | ③ | ④ | ④ |

| 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ① | ① | ② | ④ | ③ | ③ | ④ | ① | ③ | ④ |

| 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ② | ② | ① | ② | ④ | ④ | ③ | ① | ④ | ② |

| 71 | 72 | 73 | 74 | 75 |
| --- | --- | --- | --- | --- |
| ③ | ① | ④ | ④ | ① |


---

## Question 1

Is it possible to Expose a REST API in OutSystems?

- [x] **A. Yes**
- [ ] B. No

> **Explanation**
> **Answer:** A
> OutSystems 플랫폼에서는 REST API를 노출(Expose)할 수 있습니다. 이를 통해 외부 시스템이
> OutSystems 애플리케이션과 통신할 수 있도록 API를 제공할 수 있습니다. 따라서 정답은 **A.
> Yes**입니다.

---

## Question 2

Select the correct option regarding the Input Widget.

- [ ] A. All input widgets must be inside a Form widget.
- [ ] B. You don't need to have a variable. The data typed by the user is saved in the Input widget itself.
- [ ] C. It can only be associated to variables of Text data type.
- [x] **D. You always need to have a variable to store the value typed by the user.**

> **Explanation**
> **Answer:** D
> OutSystems에서 Input Widget은 사용자가 입력한 데이터를 저장하기 위해 반드시 변수(Variable)
> 와 연결되어야 합니다. 입력된 데이터는 Input Widget 자체에 저장되지 않고, 연결된 변수에 저장
> 됩니다. 따라서 정답은 **D. You always need to have a variable to store the value typed by the
> user**입니다.

---

## Question 3

In Rich Widgets, the List_Navigation widget…..

- [x] **A. Is a navigator for a Table Records with multiple pages, showing a defined number of elements per page.**
- [ ] B. Is a navigator for a Form with multiple pages, showing a defined number of elements per page.

> **Explanation**
> **Answer:** A
> List_Navigation 위젯은 OutSystems의 Rich Widgets에 포함된 것으로, Table Records를 페이지 단
> 위로 나누어 표시하고 페이지 간 탐색을 지원하는 위젯입니다. Form과는 관련이 없으므로 정답은
> **A. Is a navigator for a Table Records with multiple pages, showing a defined number of elements
> per page**입니다.

---

## Question 4

Regarding Expression on the screen, which of the following options is true?

- [ ] A. Expression can call server action and use the server action output to calculate
- [ ] B. If the expression is empty, the value shown in the Example property will be displayed
- [x] **C. The value of Expression will be calculated during the build screen and displayed on the screen**
- [ ] D. Expression cannot call server action and uses server action output to calculate

> **Explanation**
> **Answer:** C
> OutSystems에서 Expression은 화면이 빌드될 때 계산되어 화면에 표시됩니다. Expression은 주로
> 클라이언트 측에서 계산되며, 서버 액션을 직접 호출하지는 않습니다. 따라서 정답은 **C. The
> value of Expression will be calculated during the build screen and displayed on the screen**입니다.

---

## Question 5

Style classes can be overriden, so if you have the same style class defined in a Web Block, a Screen, and the Theme, which definition is applied?

- [ ] A. The one in the Web Block.
- [x] **B. The one in the Screen.**
- [ ] C. The one in the Theme.
- [ ] D. The one in the UI Flow.

> **Explanation**
> **Answer:** B
> OutSystems에서 스타일 클래스는 계층 구조에 따라 우선순위가 결정됩니다. 동일한 스타일 클래
> 스가 Web Block, Screen, Theme에 정의된 경우, 가장 구체적인 수준인 **Screen**에 정의된 스타
> 일이 우선적으로 적용됩니다. 따라서 정답은 **B. The one in the Screen**입니다.

---

## Question 6

When doing a "With or Without" join between tow entities, it returns..

- [ ] A. All records from both entities(FULL OUTER JOIN)
- [ ] B. Only records where there is match between the tow entities(INNER JOIN)
- [x] **C. All records from the left entity even if there is no match in the right entity(LEFT JOIN)**
- [ ] D. All records from the right entity even if there is no match in the left entity(RIGHT JOIN)

> **Explanation**
> **Answer:** C
> OutSystems에서 "With or Without" 조인은 SQL의 LEFT JOIN에 해당합니다. 이는 왼쪽 엔티티의
> 모든 레코드를 반환하며, 오른쪽 엔티티에 매칭되는 레코드가 없더라도 왼쪽 엔티티의 레코드는
> 포함됩니다. 따라서 정답은 **C. All records from the left entity even if there is no match in the right
> entity(LEFT JOIN)**입니다.

---

## Question 7

Regarding List_SortColumn, which of the following options is true?

- [x] **A. Set the Column to '{EntityName}.[AttributeName]' & define a dynamic sort**
- [ ] B. Set the Column to '{EntityName}.[AttributeName]' & Automatic add a dynamic sort
- [ ] C. Set the Column to '{EntityName}.{AttributeName}' & define a dynamic sort
- [ ] D. Set the Column to '{EntityName}.{AttributeName}' & Automatic add a dynamic sort

> **Explanation**
> **Answer:** A
> List_SortColumn 위젯은 동적 정렬을 정의하기 위해 사용됩니다. 이때 Column 속성은
> `{EntityName}.[AttributeName]` 형식으로 설정해야 하며, 개발자가 동적 정렬을 명시적으로 정의해
> 야 합니다. 자동으로 동적 정렬이 추가되지는 않습니다. 따라서 정답은 **A. Set the Column to
> '{EntityName}.[AttributeName]' & define a dynamic sort**입니다.

---

## Question 8

Entities and Attributes are created in the database as...

- [x] **A. Tables and Columns**
- [ ] B. Tables and Indexes
- [ ] C. Indexes and Columns
- [ ] D. Tables and Constraints

> **Explanation**
> **Answer:** A
> OutSystems에서 엔티티(Entity)는 데이터베이스에서 테이블(Table)로 생성되며, 엔티티의 속성
> (Attribute)은 해당 테이블의 컬럼(Column)으로 생성됩니다. 따라서 정답은 **A. Tables and
> Columns**입니다.

---

## Question 9

To speed up application development, OutSystems has pre-built screens with logic and data for typical scenarios

- [x] **A. TRUE**
- [ ] B. FALSE

> **Explanation**
> **Answer:** A
> OutSystems는 애플리케이션 개발 속도를 높이기 위해 일반적인 시나리오에 맞는 사전 제작된 화
> 면(Pre-built Screens)과 로직, 데이터를 제공합니다. 예를 들어, 목록 화면이나 상세 화면 등을 쉽
> 게 생성할 수 있습니다. 따라서 정답은 **A. TRUE**입니다.

---

## Question 10

The Check Box widget is bound to a Variable of type.

- [ ] A. Text
- [ ] B. Integer
- [x] **C. Boolean**
- [ ] D. Date

> **Explanation**
> **Answer:** C
> Check Box 위젯은 사용자가 선택하거나 선택 해제할 수 있는 이진 상태를 나타내며, 이는
> Boolean 타입(참/거짓) 변수와 연결됩니다. 따라서 정답은 **C. Boolean**입니다.

---

## Question 11

Consider a Web Screen with a Button that is associated to a Screen Action. An Ajax Refresh statement in that Screen Action allows to refresh part of that Web Screen, ...

- [ ] A. if the button has Method Navigate.
- [ ] B. regardless of the Button's Method.
- [x] **C. if the Button has Method Ajax Submit.**
- [ ] D. if the Button has Method Submit.

> **Explanation**
> **Answer:** C
> Ajax Refresh는 화면의 특정 부분만 새로고침하는 데 사용됩니다. 이는 버튼의 Method가 **Ajax
> Submit**으로 설정된 경우에 가능합니다. Navigate는 화면 전환, Submit은 전체 페이지 새로고침
> 을 유발하므로 Ajax Refresh와 관련이 없습니다. 따라서 정답은 **C. if the Button has Method Ajax
> Submit**입니다.

---

## Question 12

When you want to display a widget in a certain role, what is the best way?

- [ ] A. The widget's Visible property setting is Check < RoleName> Role (UserId) = True
- [ ] B. Use Container to display control with Display property as Check < RoleName> Role (UserId) = True
- [x] **C. Use the If condition to display control provided that Check < RoleName> Role (UserId) = True**
- [ ] D. Cannot perform the display in units of each widget, so it cannot be done

> **Explanation**
> **Answer:** C
> 특정 역할(Role)에 따라 위젯을 표시하려면 **If 조건**을 사용하여 해당 역할이 참인지 확인하는
> 것이 가장 적합합니다. If 위젯을 사용하면 조건에 따라 위젯을 동적으로 표시하거나 숨길 수 있습
> 니다. Visible 속성이나 Container의 Display 속성은 직접적으로 역할 체크를 지원하지 않습니다.
> 따라서 정답은 **C. Use the If condition to display control provided that Check < RoleName> Role
> (UserId) = True**입니다.

---

## Question 13

Output parameters are available ...

- [ ] A. Only inside their implementation scope.
- [ ] B. Only outside their implementation scope.
- [x] **C. Both inside and outside their implementation scope.**

> **Explanation**
> **Answer:** C
> OutSystems에서 출력 매개변수(Output Parameters)는 액션의 구현 범위 내에서도 사용 가능하며,
> 해당 액션을 호출한 외부 범위에서도 사용할 수 있습니다. 따라서 정답은 **C. Both inside and
> outside their implementation scope**입니다.

---

## Question 14

Regarding Web Blocks in Outsystems, select to statement that is true.

- [ ] A. Web Block can only have 1 output
- [ ] B. Web Block cannot have preparation action
- [x] **C. Web Block can Preparation action**
- [ ] D. Web Block can have multiple outputs

> **Explanation**
> **Answer:** C
> Web Block은 OutSystems에서 재사용 가능한 UI 구성 요소로, Preparation 액션을 가질 수 있습니
> 다. Preparation 액션은 Web Block이 렌더링되기 전에 데이터를 준비하는 데 사용됩니다. Web
> Block은 여러 출력 매개변수를 가질 수 없으며, Preparation 액션은 필수가 아닙니다. 따라서 정답
> 은 **C. Web Block can Preparation action**입니다.

---

## Question 15

Consider a Web Screen with a Button that is associated to a Screen Action. An Ajax Refresh statement in that Screen Action allows to refresh part of that Web Screen, ...

- [ ] A. if the button has Method Navigate.
- [ ] B. regardless of the Button's Method.
- [x] **C. if the Button has Method Ajax Submit.**
- [ ] D. if the Button has Method Submit.

> **Explanation**
> **Answer:** C
> Ajax Refresh는 화면의 특정 부분만 새로고침하는 데 사용됩니다. 이는 버튼의 Method가 **Ajax
> Submit**으로 설정된 경우에 가능합니다. Navigate는 화면 전환, Submit은 전체 페이지 새로고침
> 을 유발하므로 Ajax Refresh와 관련이 없습니다. 따라서 정답은 **C. if the Button has Method Ajax
> Submit**입니다.

---

## Question 16

When the desired data type is Currency, the following data type transmission does not occur(error)

- [ ] A. Decimal, Integer, Long Integer
- [ ] B. Long Integer, Integer, Boolean, Entity Identifier(Integer)
- [ ] C. Decimal, Long Integer, Boolean, Entity Identifier(Integer)
- [x] **D. Decimal, Integer, Boolean, Entity Identifier(Integer)**

> **Explanation**
> **Answer:** D
> Currency 데이터 타입은 주로 Decimal로 처리되며, Integer, Boolean, Entity Identifier(Integer)로의
> 변환은 오류 없이 가능합니다. 그러나 Long Integer는 Currency로 변환 시 정밀도 문제로 오류가
> 발생할 수 있습니다. 따라서 오류가 발생하지 않는 조합은 **D. Decimal, Integer, Boolean, Entity
> Identifier(Integer)**입니다.

---

## Question 17

What is the correct syntax for writing names of Entities and Entity Attributes in SQL Query

- [ ] A. <Entity> and <Entity>.[Attribute]
- [ ] B. {Entity} and {Entity}.{Attribute}
- [x] **C. {Entity} and {Entity}.[Attribute]**
- [ ] D. <Entity> and <Entity>.<Attribute>

> **Explanation**
> **Answer:** C
> OutSystems에서 SQL 쿼리 작성 시 엔티티와 속성 이름은 `{Entity}.[Attribute]` 형식으로 작성해야
> 합니다. 이는 OutSystems의 표준 구문입니다. 따라서 정답은 **C. {Entity} and {Entity}.[Attribute]**
> 입니다.
> ---

---

## Question 18

What types of applications can be created in OutSystems?

- [x] **A. Web, Mobile and Service**
- [ ] B. Web, Mobile, Service and Extension
- [ ] C. Module and Extension
- [ ] D. Only Web

> **Explanation**
> **Answer:** A
> OutSystems에서는 Web, Mobile, Service 애플리케이션을 생성할 수 있습니다. Extension은 별도의
> 모듈 타입으로 간주되지 않으며, Module은 애플리케이션의 구성 요소일 뿐입니다. 따라서 정답은
> **A. Web, Mobile and Service**입니다.

---

## Question 19

What is the output of an aggregate when no records meet the criteria?

- [ ] A. Null List
- [x] **B. Empty list**
- [ ] C. List has an empty record
- [ ] D. List has a record with default data

> **Explanation**
> **Answer:** B
> OutSystems에서 Aggregate가 기준을 충족하는 레코드를 찾지 못하면 빈 리스트(Empty List)를 반
> 환합니다. Null이나 기본 데이터가 포함된 레코드는 반환되지 않습니다. 따라서 정답은 **B. Empty
> list**입니다.

---

## Question 20

The Check Box widget is bound to a Variable of type...

- [ ] A. Text
- [ ] B. Integer
- [x] **C. Boolean**
- [ ] D. Date

> **Explanation**
> **Answer:** C
> Check Box 위젯은 사용자가 선택하거나 선택 해제할 수 있는 이진 상태를 나타내며, 이는
> Boolean 타입(참/거짓) 변수와 연결됩니다. 따라서 정답은 **C. Boolean**입니다.

---

## Question 21

Create unique customer index with 2 fields Name and Email. When performing any insert data below, an error will occur

- [ ] A. (Jonh,jonh@gmail.com,1122),(Jonh_Hand,jonh@gmail.com,1122)
- [ ] B. (Jonh,jonh@gmail.com,1122),(Jonh,jonh_hand@gmail.com,1122)
- [ ] C. (Jonh,jonh@gmail.com,1122),(Jonh_Hand,jonh@gmail.com,3344)
- [x] **D. (Jonh,jonh@gmail.com,1122),(Jonh,jonh@gmail.com,3344)**

> **Explanation**
> **Answer:** D
> Name과 Email 필드에 대해 고유 인덱스(Unique Index)를 생성하면, 동일한 Name과 Email 조합이
> 삽입될 때 오류가 발생합니다. 옵션 D에서는 `(Jonh, jonh@gmail.com)`이 두 번 삽입되므로 고유
> 제약 조건을 위반하여 오류가 발생합니다. 따라서 정답은 **D.
> (Jonh,jonh@gmail.com,1122),(Jonh,jonh@gmail.com,3344)**입니다.

---

## Question 22

Regarding exposing elements in Producer modules...

- [ ] A. Any element can be exposed, and reused, but only by modules of the same application.
- [ ] B. Any element can be exposed, and reused by modules of any application.
- [x] **C. Only elements with the Public property set to Yes can be exposed and reused by modules of any application.**
- [ ] D. Only elements with the Public property set to Yes can be exposed and reused, but only by modules of the same application.

> **Explanation**
> **Answer:** C
> Producer 모듈에서 요소를 노출(Expose)하려면 해당 요소의 Public 속성이 Yes로 설정되어야 합니
> 다. Public으로 설정된 요소는 동일 애플리케이션뿐만 아니라 다른 애플리케이션의 모듈에서도 재
> 사용할 수 있습니다. 따라서 정답은 **C. Only elements with the Public property set to Yes can be
> exposed and reused by modules of any application**입니다.

---

## Question 23

To restrict access to a Web Screen...

- [ ] A. Go to the Users application and associate the Web Screen to a specific role.
- [x] **B. Select the Role in the Web Screen Properties pane and OutSystems will automatically check the Role at runtime.**

> **Explanation**
> **Answer:** B
> Web Screen의 접근을 제한하려면 Web Screen 속성 패널에서 특정 역할(Role)을 선택하면 됩니다.
> OutSystems는 런타임에 해당 역할을 자동으로 확인하여 접근을 제어합니다. 따라서 정답은 **B.
> Select the Role in the Web Screen Properties pane and OutSystems will automatically check the
> Role at runtime**입니다.

---

## Question 24

A Theme defines the look and feel of application Screens and you can directly apply it to ...

- [ ] A. A Module, a UI Flow, or an individual Screen or Web Block.
- [ ] B. A Module, a UI Flow, or an individual Screen.
- [x] **C. A Module or a UI Flow.**
- [ ] D. Only the Module.

> **Explanation**
> **Answer:** C
> OutSystems에서 Theme은 애플리케이션의 모양과 느낌을 정의하며, Module 또는 UI Flow에 직접
> 적용할 수 있습니다. 개별 Screen이나 Web Block에는 직접 적용되지 않고, Module 또는 UI Flow
> 의 Theme 설정을 따릅니다. 따라서 정답은 **C. A Module or a UI Flow**입니다.

---

## Question 25

Regarding property Escape Content of Expression, which of the following options is true?

- [x] **A. When set to No, the result returns exactly as the result of the formula**
- [ ] B. When set to Yes, the result returns exactly as the result of the formula
- [ ] C. When the value is No, the special characters in the returned result have been replaced by characters that do not affect the protocol being used.
- [ ] D. The default value is No

> **Explanation**
> **Answer:** A
> Expression의 Escape Content 속성은 출력 결과의 특수 문자를 처리하는 방식을 정의합니다.
> **No**로 설정하면 결과는 공식 그대로 반환되며, 특수 문자가 이스케이프되지 않습니다. **Yes**
> 로 설정하면 특수 문자가 프로토콜에 영향을 주지 않도록 이스케이프됩니다. 따라서 정답은 **A.
> When set to No, the result returns exactly as the result of the formula**입니다.

---

## Question 26

Regarding Session Variable, which of the following options is true?

- [ ] A. Set persistent property to true, the session can be shared for the entire system to use
- [ ] B. Session variables can only use basic data types (Integer, Text, Boolean,...)
- [x] **C. The session variable will expire when the session times out**
- [ ] D. Set Cache property to store session value after user log out

> **Explanation**
> **Answer:** C
> 세션 변수(Session Variable)는 사용자의 세션이 유지되는 동안 데이터를 저장하는 데 사용됩니다.
> 세션이 만료되면 세션 변수도 함께 사라집니다. Persistent 속성은 데이터베이스 저장과 관련이 있
> 으며, Cache 속성은 세션 변수와 관련이 없습니다. 따라서 정답은 **C. The session variable will
> expire when the session times out**입니다.

---

## Question 27

To create a List screen and then a Detail screen...

- [ ] A. Drag and drop an Entity to the UI Flow and it automatically creates the List and Detail Screens.
- [x] **B. Drag and drop an Entity to the UI Flow to create the List Screen and repeat it to create the Detail Screen.**

> **Explanation**
> **Answer:** B
> OutSystems에서 List Screen과 Detail Screen을 생성하려면, UI Flow에 엔티티를 드래그 앤 드롭하
> 여 List Screen을 먼저 생성하고, 동일한 과정을 반복하여 Detail Screen을 생성해야 합니다. 자동으
> 로 두 화면이 동시에 생성되지는 않습니다. 따라서 정답은 **B. Drag and drop an Entity to the UI
> Flow to create the List Screen and repeat it to create the Detail Screen**입니다.

---

## Question 28

In any case, should use Site property

- [x] **A. Minimum password length**
- [ ] B. Number of logged user
- [ ] C. Search field value

> **Explanation**
> **Answer:** A
> Site 속성은 애플리케이션 전반에 걸쳐 사용되는 전역 설정을 정의하는 데 사용됩니다. 예를 들어,
> **Minimum password length**는 모든 사용자에게 적용되는 보안 정책으로 Site 속성에 적합합니
> 다. 반면, 로그인한 사용자 수나 검색 필드 값은 동적 데이터로 Site 속성에 적합하지 않습니다.
> 따라서 정답은 **A. Minimum password length**입니다.

---

## Question 29

A Structure can have attributes of the following data types:

- [ ] A. Basic, Complex, and Record
- [ ] B. Basic, String, and Object
- [x] **C. Basic, Structure, Entity, and List**
- [ ] D. Basic and List only

> **Explanation**
> **Answer:** C
> OutSystems에서 Structure는 다양한 데이터 타입의 속성을 가질 수 있습니다. 지원되는 데이터 타
> 입은 기본 타입(Basic), Structure, Entity, List입니다. Complex나 Object는 OutSystems에서 사용되지
> 않는 용어입니다. 따라서 정답은 **C. Basic, Structure, Entity, and List**입니다.

---

## Question 30

What types of applications can be created in OutSystems?

- [x] **A. Web, Mobile and Service**
- [ ] B. Web, Mobile, Service and Extension
- [ ] C. Module and Extension
- [ ] D. Only Web

> **Explanation**
> **Answer:** A
> OutSystems에서는 Web, Mobile, Service 애플리케이션을 생성할 수 있습니다. Extension은 별도의
> 모듈 타입으로 간주되지 않으며, Module은 애플리케이션의 구성 요소일 뿐입니다. 따라서 정답은
> **A. Web, Mobile and Service**입니다.

---

## Question 31

Style load order

- [ ] A. Screen & Email -> Web block -> theme
- [ ] B. theme -> Web block -> Screen & Email
- [x] **C. Web block -> theme -> Screen & Email**

> **Explanation**
> **Answer:** C
> OutSystems에서 스타일 로드 순서는
> 1. System style sheet for Container widgets in the Grid.
> 2. Block style sheet.
> 3. Theme style sheet, which also includes a base theme (if specified).
> 4. Screen or Email style sheet.
> 5. Theme extra style sheet, with the Grid settings defined in the Theme properties.
> 6. Styles that Service Studio generates when you use Styles Editor.
> 7. Inline style you define in Attributes or Extended Properties.

---

## Question 32

Regarding Preparation in Outsystems, select to statement that is true.

- [ ] A. Preparation action may have multiple outputs
- [ ] B. Preparation is a forced action of Screen and webBlock
- [ ] C. The preparation action can only have 1 output
- [x] **D. Screen may not need Preparation**

> **Explanation**
> **Answer:** D
> Preparation 액션은 Screen 또는 Web Block이 렌더링되기 전에 데이터를 준비하는 데 사용됩니다.
> 하지만 모든 Screen이 Preparation 액션을 필요로 하지는 않습니다. Preparation 액션은 여러 출력
> 매개변수를 가질 수 있으며, 필수 액션은 아닙니다. 따라서 정답은 **D. Screen may not need
> Preparation**입니다.

---

## Question 33

Roles are created in applications and user authorizations are managed...

- [x] **A. Manually in the Users application or programmatically.**
- [ ] B. Only manually in the Users application.
- [ ] C. Only programmatically using the Grant... and Revoke... role actions.

> **Explanation**
> **Answer:** A
> OutSystems에서 역할(Role)은 애플리케이션 내에서 생성되며, 사용자 권한은 Users 애플리케이션
> 을 통해 수동으로 관리하거나, Grant 및 Revoke 역할 액션을 사용하여 프로그래밍적으로 관리할
> 수 있습니다. 따라서 정답은 **A. Manually in the Users application or programmatically**입니다.

---

## Question 34

When consuming a REST service, what callback action should be used to customize a request sent to the external service?

- [ ] A. On Consume
- [x] **B. On Before Request**
- [ ] C. On After Response
- [ ] D. On REST Request

> **Explanation**
> **Answer:** B
> REST 서비스를 소비할 때 요청을 커스터마이징하려면 **On Before Request** 콜백 액션을 사용해
> 야 합니다. 이 액션은 요청이 외부 서비스로 전송되기 전에 실행되어 요청 헤더나 페이로드를 수
> 정할 수 있습니다. 따라서 정답은 **B. On Before Request**입니다.

---

## Question 35

When there is a change in the Producer module, which statement later about the Consumer module is correct.

- [x] **A. When adding the output of Server action, the consumer will get an error if the Producer is not updated**
- [ ] B. When changing the internal logic of a server action without changing the input-output, Consumer still uses the latest logic
- [ ] C. When deleting the input of the Server action, the consumer will get an error if the Producer is not updated
- [ ] D. When changing the content of the web screen, the Consumer is still not affected even without updating Producer

> **Explanation**
> **Answer:** A
> Producer 모듈에서 서버 액션의 출력 매개변수를 추가하면, Consumer 모듈은 Producer가 업데이
> 트되지 않으면 참조 오류가 발생합니다. 내부 로직 변경은 입력-출력이 동일하다면 영향을 주지
> 않으며, 웹 화면 변경은 Consumer에 직접적인 영향을 주지 않습니다. 따라서 정답은 **A. When
> adding the output of Server action, the consumer will get an error if the Producer is not updated**
> 입니다.

---

## Question 36

Inside the Preparation of Web Screen, the Destination statement...

- [ ] A. . cannot be used.
- [x] **B. allows redirecting the user to a different Web Screen, without rendering the current Screen.**
- [ ] C. renders the Current Screen and afterwards the users is redirected to the Destination Screen.
- [ ] D. prompts the user before redirecting to the Destination Web Screen

> **Explanation**
> **Answer:** B
> Web Screen의 Preparation에서 Destination 문은 현재 화면을 렌더링하지 않고 사용자를 다른 화
> 면으로 리디렉션합니다. 이는 조건에 따라 즉시 다른 화면으로 이동할 때 사용됩니다. 따라서 정
> 답은 **B. allows redirecting the user to a different Web Screen, without rendering the current
> Screen**입니다.

---

## Question 37

Consider that you want to change your application Header, with new fonts, colors and an icon. What is the best approach to accomplish that in Outsystems?

- [ ] A. Change the Common/Header Web Block, by adding a Container with the new icon. Add the new CSS to the Module Theme's Style Sheet.
- [ ] B. Add the new CSS to the Style Sheet of every Web Screens in the application, overriding the Style Sheet of the Common/Header Web Block Replace the Header_Logo with the new icon.
- [x] **C. Change the Style Sheet of the Common/Header Web Block, with the new CSS implemented and replace the Header_Logo with the new icon.**
- [ ] D. Replace the Common/Header Web Block on every Web Screen with a new Web Block containing the new icon and CSS in its Style Sheet.

> **Explanation**
> **Answer:** C
> 애플리케이션의 헤더를 변경하려면 공통적으로 사용되는 **Common/Header Web Block**의 스타
> 일 시트(Style Sheet)를 수정하고, 로고(Header_Logo)를 새로운 아이콘으로 교체하는 것이 가장 효
> 율적입니다. 모든 화면에 개별적으로 CSS를 추가하거나 Web Block을 교체하는 것은 비효율적입
> 니다. 따라서 정답은 **C. Change the Style Sheet of the Common/Header Web Block, with the new
> CSS implemented and replace the Header_Logo with the new icon**입니다.

---

## Question 38

XXX screen only Registered role is checked, which of the following statements is true?

- [x] **A. User has not logged in, make request Screen XXX. As a result, can not permission**
- [ ] B. User logged, make request Screen XXX. As a result, can not permission

> **Explanation**
> **Answer:** A
> XXX 화면에 **Registered** 역할만 체크되어 있다면, 해당 화면에 접근하려면 사용자가 로그인하
> 여 Registered 역할을 가져야 합니다. 로그인하지 않은 사용자가 요청하면 권한이 없어 접근할 수
> 없습니다. 따라서 정답은 **A. User has not logged in, make request Screen XXX. As a result, can
> not permission**입니다.

---

## Question 39

Regarding a Consumer module

- [ ] A. It can only reuse elements from Producer modules of the same application.
- [x] **B. It can only reuse elements that are Public in their Producer modules.**
- [ ] C. It can reuse any element from any Producer module.
- [ ] D. It can only reuse elements from Producer modules of other applications.

> **Explanation**
> **Answer:** B
> Consumer 모듈은 Producer 모듈의 요소를 재사용할 수 있지만, 해당 요소가 **Public**으로 설정
> 되어 있어야 합니다. Public이 아닌 요소는 재사용할 수 없으며, 동일 애플리케이션이나 다른 애플
> 리케이션에 관계없이 Public 요소만 가능합니다. 따라서 정답은 **B. It can only reuse elements that
> are Public in their Producer modules**입니다.

---

## Question 40

Give 1 aggregate as shown. Ask how to display the average score of the group according to Point1 and sort the order of Point 2 with the highest score by year

- [ ] A. Use the GROUPBY function according to the Year attribute, then perform the AVERAGE function for the Point 1 attribute and MAX for the attribute for Point 2.
- [x] **B. Use the GROUPBY function according to the Group attribute, then perform the AVERAGE function for the Point 1 attribute and MAX for the attribute for Point 2.**
- [ ] C. Use the GROUPBY function according to the Year attribute, then perform the AVERAGE function for the Point 2 attribute and MAX for the Point 1 attribute.
- [ ] D. Use the GROUPBY function according to the Group attribute, then perform the AVERAGE function for the Point 2 attribute and MAX for the attribute for Point 1.

> **Explanation**
> **Answer:** B
> Aggregate를 사용하여 그룹별 평균 점수(Point1)를 표시하고, Point2의 최고 점수를 기준으로 연도
> 별 정렬하려면, **Group** 속성으로 GROUPBY를 수행한 후, Point1에 대해 AVERAGE 함수를,
> Point2에 대해 MAX 함수를 적용해야 합니다. Year로 그룹화하면 요구사항과 맞지 않습니다. 따라
> 서 정답은 **B. Use the GROUPBY function according to the Group attribute, then perform the
> AVERAGE function for the Point 1 attribute and MAX for the attribute for Point 2**입니다.

---

## Question 41

To replace data on a widget with automatic data replacement (Tables Records, List Records, Form,...)

- [ ] A. Right-click on the widget and select Import Data from Entity
- [ ] B. Delete the widget and create it again with the right Entities.
- [x] **C. Drag your Entity and drop it onto the widget.**
- [ ] D. Right-click on the Entity and select Import Data from Excel.

> **Explanation**
> **Answer:** C
> OutSystems에서 Table Records, List Records, Form 등의 위젯에 데이터를 자동으로 교체하려면, 엔
> 티티(Entity)를 위젯 위로 드래그 앤 드롭하면 됩니다. 이는 데이터를 위젯에 바인딩하는 가장 직
> 관적이고 효율적인 방법입니다. 따라서 정답은 **C. Drag your Entity and drop it onto the widget**
> 입니다.

---

## Question 42

When an OnParameterChange event will trigger?

- [ ] A. When the block changes the value of any input parameter of itself.
- [ ] B. When the parent of the block or block itself changes the value of the block's input parameter.
- [x] **C. When the parent of the block changes the value of any of the block's input parameters.**
- [ ] D. If the value of a Block's Input Parameters changes inside a Client Action of the Block.

> **Explanation**
> When the parent of the block changes the value of any of the block's input parameters.
> OnParameterChange will only trigger when any of block's input parameter value is changed from
> parent of block. Parent can be both screen or other block.
> `OnParameterChange` 이벤트는 블록의 입력 매개변수 값이 부모(화면 또는 다른 블록)에 의해 변
> 경될 때만 트리거됩니다. 따라서 정답은 **"When the parent of the block changes the value of any
> of the block's input parameters."**입니다. 블록 자체가 값을 변경하거나 클라이언트 액션 내부에서
> 값이 변경되는 경우에는 이벤트가 발생하지 않습니다.

---

## Question 43

If in an entity, a reference attribute is defined with protect rule then what is the correct statement?

- [x] **A. It would not allow deleting rows from the parent entity in case of reference data is available in the child table.**
- [ ] B. It would protect entities from cyber attacks.
- [ ] C. It would not allow deletion row from the parent table in every case.
- [ ] D. It would protect the entity to perform a delete operation on itself.

> **Explanation**
> It would not allow deleting rows from the parent entity in case of reference data is
> available in the child table.
> 엔터티에서 참조 속성이 `Protect` 규칙으로 정의된 경우, 자식 테이블에 참조 데이터가 존재하면
> 부모 엔터티의 행을 삭제할 수 없습니다. 이는 참조 무결성을 유지하기 위한 제약입니다.

---

## Question 44

Which of the following is not possible to fetch when the screen is initializing?

- [x] **A. Advanced SQL in the screen level**
- [ ] B. Aggregates in the screen level.
- [ ] C. Aggregates inside the data action flow
- [ ] D. Rest API in the data action flow.

> **Explanation**
> Advanced SQL in the screen level
> Advanced SQL can only be used in server action or Inside Data Actions.
> 화면 초기화 시, `Advanced SQL`은 화면 수준에서 직접 가져올 수 없으며, 서버 액션이나 데이터
> 액션 내에서만 사용할 수 있습니다. 반면, 화면 수준의 `Aggregates`, 데이터 액션 흐름 내의
> `Aggregates`, 그리고 `Rest API`는 초기화 시 가져올 수 있습니다

---

## Question 45

Why should we not call multiple server actions in one client action?

- [ ] A. Because there is a risk of cyber-attacks?
- [x] **B. It gives a performance problem and may slow down the application processing**
- [ ] C. It can cause incorrect data operation.
- [ ] D. It can cause data issues.

> **Explanation**
> It gives a performance problem and may slow down the application processing
> Calling multiple server action may slow down the application processing as it gives multiple call to
> server which gives performance troubles.
> 클라이언트 액션에서 여러 서버 액션을 호출하면 서버에 다중 호출이 발생하여 성능 문제가 발생
> 하고 애플리케이션 처리 속도가 느려질 수 있습니다.

---

## Question 46

Choose the correct option associated with the below ERD?

- [x] **A. OrderType Can not have SellOrderId attribute**
- [ ] B. No mapping can be formed between both entities.
- [ ] C. OrderType should be a normal entity.
- [ ] D. SellOrder can not have OrderType attribute.

> **Explanation**
> OrderType Can not have SellOrderId attribute
> A normal Entity's identifier cannot be referenced in a Static entity.
> 정적 엔터티(Static Entity)는 일반 엔터티(Normal Entity)의 식별자를 참조 속성으로 가질 수 없습니
> 다. 이는 OutSystems의 정적 엔터티가 고정된 데이터만 포함하며, 동적 참조를 허용하지 않는 설
> 계 제약 때문입니다.

---

## Question 47

Is it possible to define entity identifier other then LongInteger data type?

- [ ] A. Yes
- [ ] B. No
- [x] **C. Yes, But it can be only Text, Integer, LongInteger, and Entity Identifier**
- [ ] D. Yes, but it can be only EntityIdentifier

> **Explanation**
> Yes, But it can be only Text, Integer, LongInteger, and Entity Identifier
> Entity Identifier can be set as Text, Integer, Long Integer, and Other Entity Identifier
> OutSystems에서 엔터티 식별자는 `LongInteger`뿐만 아니라 `Text`, `Integer`, `LongInteger`, 그리고
> 다른 엔터티 식별자로 설정할 수 있습니다. 따라서 정답은 **"Yes, But it can be only Text, Integer,
> LongInteger, and Entity Identifier"**입니다.

---

## Question 48

Which of the following is true about the 'On Render' event?

- [ ] A. It triggered before the onReady event.
- [ ] B. It is the first event to be triggered when we navigate from one screen to other.
- [x] **C. It runs every time when there is any change in the data on the screen.**
- [ ] D. It runs only once after the page is ready.

> **Explanation**
> It runs every time when there is any change in the data on the screen.
> OnRender event triggered every time when there is any change in the data on the screen.
> OutSystems에서 `On Render` 이벤트는 화면의 렌더링이 완료된 후 발생하며, `OnReady` 이벤트(화
> 면의 모든 요소가 준비된 후)보다 **나중에** 트리거됩니다.

---

## Question 49

Which statement about entities is false?

- [ ] A. Entities do not require an Identifier
- [ ] B. Entities can be deleted
- [ ] C. Entities can be set as multitenant
- [x] **D. Entities are stored in memory**

> **Explanation**
> Entities are stored in memory
> 엔터티는 데이터베이스에 테이블로 저장되며, 메모리에 저장되지 않습니다. 따라서 **"Entities are
> stored in memory"**는 거짓입니다. 엔터티는 식별자를 필요로 하며, 삭제 가능하고, 멀티테넌트로
> 설정할 수 있습니다.

---

## Question 50

Which of the option below is true when any of the mandatory input's valid property is false?

- [ ] A. Form.valid will be true.
- [ ] B. We would require to set form.valid property false explicitly.
- [ ] C. Form.valid will be unchanged.
- [x] **D. The form's valid property will automatically be set to false.**

> **Explanation**
> The form's valid property will automatically be set to false.
> 필수 입력 필드의 `Valid` 속성이 `False`인 경우, 폼 전체의 `Valid` 속성도 자동으로 `False`로 설정
> 됩니다. 이는 OutSystems의 폼 유효성 검사 메커니즘 때문입니다. 따라서 정답은 **"valid
> property will automatically be set to false."**입니다.

---

## Question 51

A client action is set to its public and function property set to "NO", This action can be....

- [x] **A. Can be called a Screen Action.**
- [ ] B. Can be called from a Server Action.
- [ ] C. Can be used in an Expression
- [ ] D. Can be called from other modules.

> **Explanation**
> Can be called a Screen Action.
> If function property set to yes than only it can be called in an expression, and if public property is
> set to be yes then only it can be called from other module. And client action can not be called from
> server action.
> 클라이언트 액션의 `Public` 속성이 `No`이고 `Function` 속성이 `No`인 경우, 해당 액션은 다른 모
> 듈에서 호출될 수 없습니다. `Function` 속성이 `No`이므로 표현식(Expression)에서 호출할 수 없으
> 며, 클라이언트 액션은 서버 액션에서 호출될 수 없습니다.

---

## Question 52

What would be the value of FinalValue in the below logic?

- [x] **A. FinalValue will be the default value or equal to the 'Value'.**
- [ ] B. The FinalValue will be the default value assigned to it.
- [ ] C. The value of FinalValue is always 5.
- [ ] D. The value of the FinalValue will be greater than 5.

> **Explanation**
> FinalValue will be the default value or equal to the 'Value'.
> 최종값은 Value와 FinalValue 가 다를 수 있으나 다른 선택지가 모두 오답이고 일시적으로는 같은
> 값으로 설정 될 것임.

---

## Question 53

When the built-in validation is set to true, in which condition form will be submitted?

- [ ] A. When the Integer field, is filled with a Text value.
- [x] **B. When all non-mandatory fields are not filled.**
- [ ] C. When the date filed is filled with an Integer value.
- [ ] D. When some of the mandatory fields are not filled.

> **Explanation**
> When all non-mandatory fields are not filled.
> When built-in validation is set to true in that case all the mandatory fields should be correctly filled.
> `Built-in Validation`이 `True`로 설정된 경우, 폼은 모든 필수 필드가 올바르게 채워졌을 때만 제출
> 됩니다. 따라서 잘못된 데이터 유형(예: Integer 필드에 Text 값)이나 필수 필드가 채워지지 않은
> 경우 폼은 제출되지 않습니다.

---

## Question 54

If there are 2 entities, User and UserDetail. If one UserDetail belongs to only one User, how can we create the one-to-One mapping between them?

- [ ] A. Make the datatype the primary key of the User entity to UserDetail Identifier.
- [ ] B. Add a new attribute in UserDetail and make its data type User Identifier.
- [ ] C. Add a new attribute in User and make its data type as UserDetail Identifier.
- [x] **D. Make the Datatype of the primary key of the UserDetail entity to User Identifier.**

> **Explanation**
> Make the Datatype of the primary key of the UserDetail entity to User Identifier.
> If the Primary Key of one Entity is the primary key of another entity then it forms One to One
> Mapping.
> 일대일 매핑을 만들기 위해, `UserDetail` 엔터티의 기본 키를 `User` 엔터티의 식별자(`User
> Identifier`)로 설정해야 합니다. 이렇게 하면 `UserDetail`의 각 레코드가 정확히 하나의 `User` 레코
> 드와 연결됩니다.

---

## Question 55

We need to check if a specific element is present in the list, which list method would be used?

- [ ] A. ListIndexOf
- [ ] B. ListFilter
- [x] **C. ListAny**
- [ ] D. ListContains

> **Explanation**
> ListAny
> ListAny will check if it contains element which justify the given condition. If present it would return
> true else false.
> 리스트에 특정 요소가 있는지 확인하려면 `ListAny` 메서드를 사용합니다. 이 메서드는 주어진 조
> 건을 만족하는 요소가 리스트에 있는지 확인하여 `True` 또는 `False`를 반환합니다.

---

## Question 56

Which of the following can be set as a datatype of site property?

- [ ] A. Structure
- [ ] B. List
- [x] **C. Entity Identifier**
- [ ] D. Binary

> **Explanation**
> Entity Identifier
> Site Property Data Type can be set to any basic data type (except binary) and Entity Identifier.
> 사이트 속성(Site Property)의 데이터 유형은 기본 데이터 유형(예: Text, Integer 등)과 `Entity
> Identifier`로 설정할 수 있지만, `Binary`는 지원되지 않습니다. `Structure`와 `List`도 사이트 속성으
> 로 직접 설정할 수 없습니다.

---

## Question 57

Which programming concept is similar to the static entity?

- [ ] A. Object
- [ ] B. Map
- [ ] C. Collection
- [x] **D. Enumeration**

> **Explanation**
> Enumeration
> 정적 엔터티(Static Entity)는 고정된 데이터 집합을 나타내며, 이는 프로그래밍에서
> `Enumeration`(열거형)과 유사합니다. `Enumeration`은 미리 정의된 상수 값의 집합을 나타냅니다.

---

## Question 58

On which type of variable we can apply for each loop?

- [x] **A. List**
- [ ] B. Entity Identifier
- [ ] C. Integer
- [ ] D. Structure

> **Explanation**
> List
> In OutSystems, for each loop can be applied only on List type of variables
> OutSystems에서 `For Each` 루프는 `List` 유형의 변수에만 적용할 수 있습니다. `Entity Identifier`,
> `Integer`, `Structure`는 루프를 적용할 수 없습니다.

---

## Question 59

What is wrong in respect of the LINK widget onClick event?

- [ ] A. It can be set to an external URL
- [ ] B. It can be set to any screen in scope.
- [x] **C. It can be set to public client action.**
- [ ] D. It can be set to the current screen.

> **Explanation**
> It can be set to public client action.
> Link's and Button OnClick event property are same. OnClick property of button and link can be set
> to 1. Current Screen 2 Previous Screen 3. Screen's Client action 4. External URL.
> 링크 위젯의 `OnClick` 이벤트는 버튼의 `OnClick` 이벤트와 동일하며, 현재 화면, 이전 화면, 화면
> 의 클라이언트 액션, 외부 URL로 설정할 수 있습니다. 그러나 **공용 클라이언트 액션(Public
> Client Action)**으로 직접 설정할 수는 없습니다. 따라서 잘못된 옵션은 **"It can be set to public
> client action."**입니다.

---

## Question 60

What is the "function" property of client and server action?

- [ ] A. By setting it to yes, it would be publicly available
- [ ] B. By setting it no, it would be available to consumer modules.
- [ ] C. Its scope will be global by setting it Yes
- [x] **D. By setting yes, it would be available to call from Expression Editor**

> **Explanation**
> By setting yes, it would be available to call from Expression Editor
> 클라이언트 및 서버 액션의 `Function` 속성을 `Yes`로 설정하면, 해당 액션이 표현식 편집기
> (Expression Editor)에서 호출 가능해집니다. 이는 액션을 함수처럼 사용할 수 있게 합니다.

---

## Question 61

Which is false regarding the Static entities?

- [ ] A. It is available on the client side
- [x] **B. Records can be created at run time**
- [ ] C. It can be created at the time of development
- [ ] D. It contains records

> **Explanation**
> **Answer:** B
> 정적 엔티티(Static Entity)는 개발 시점(Development time)에 레코드가 정의되며, 런타임(Runtime)에는 레코드를 생성할 수 없습니다. 따라서 'Records can be created at run time'이 틀린 설명입니다.

---

## Question 62

What is "Expose Read Only" in respect of entity?

- [ ] A. Only Read Only Entity Identifier can be used as a reference attribute
- [x] **B. It would be exposed as read-only to the consumer modules.**
- [ ] C. It is useless property
- [ ] D. It would not allow to write anything in entity.

> **Explanation**
> **Answer:** B
> 엔티티의 'Expose Read Only' 속성을 Yes로 설정하면, 해당 엔티티를 참조하는 다른 모듈(Consumer modules)에서는 데이터를 읽을 수만 있고 직접 수정(Create, Update, Delete)할 수 없게 노출됩니다.

---

## Question 63

To ensure that the incorrect data doesn't reach the server, what is to be done? Note: Built-In validation property is set to True?

- [x] **A. Form Valid property has to be checked before adding the data to the database.**
- [ ] B. Form Valid property has to be set to false in the action flow.
- [ ] C. Nothing. Since the built-in validation is set to true.
- [ ] D. Appropriate logic should be written before sending data to the server.

> **Explanation**
> Form Valid property has to be checked before adding the data to the database.
> `Built-In Validation` 속성이 `True`로 설정된 경우, OutSystems는 자동으로 폼의 유효성을 검사하여
> 잘못된 데이터가 서버로 전송되지 않도록 합니다.

---

## Question 64

Which of the following is true with respect to the below screen setting?

- [ ] A. None Of Above
- [x] **B. No authentication is required.**
- [ ] C. Only users with valid credentials can access this screen.
- [ ] D. Only users registered with the application can access this screen.

> **Explanation**
> No authentication is required.
> As the Anonymous role is checked then there is no authentication required to access this screen,
> anyone on the web can access this screen.
> 화면의 역할에 `Anonymous`가 포함되어 있으므로, 인증 없이 누구나 웹에서 해당 화면에 접근할
> 수 있습니다.

---

## Question 65

What would be the execution order of data action and screen aggregates while loading any screen?

- [ ] A. Aggregate is first and then Data action
- [ ] B. Data action will be executed on start and aggregate will be on demand.
- [ ] C. Data Action is first and then Aggregate.
- [x] **D. Both will be executed asynchronously.**

> **Explanation**
> Both will be executed asynchronously.
> Data action and Screen aggregates are async operations.
> OutSystems에서 데이터 액션과 화면 애그리게이트는 비동기적으로 실행됩니다. 따라서 실행 순서
> 가 고정되어 있지 않으며, 둘 다 비동기 작업으로 처리됩니다. 정답은 **"Both will be executed
> asynchronously."**입니다.

---

## Question 66

If there are 2 entities, User and Group. If one User belongs to only one Group, how can we create the one-to-many mapping between them?

- [ ] A. Create a new entity User_Group and put the identifier of both user and group in the newly created entity.
- [ ] B. Create an attribute in Group with datatype as the User identifier.
- [ ] C. Create only with join in between them.
- [x] **D. Create an attribute in User with datatype as Group identifier.**

> **Explanation**
> Create an attribute in User with datatype as Group identifier.
> 일대다 매핑을 만들기 위해, `User` 엔터티에 `Group` 식별자를 데이터 유형으로 하는 속성을 추가
> 해야 합니다. 이렇게 하면 한 `Group`에 여러 `User`가 속할 수 있습니다.

---

## Question 67

Which of the following mappings between Outsystems and the database NOT is correct?

- [ ] A. Entities = Tables
- [ ] B. Attributes = Columns
- [x] **C. Referential attribute = Primary Key**
- [ ] D. Index = Index

> **Explanation**
> Referential attribute = Primary Key
> OutSystems에서 `Entities`는 데이터베이스 테이블, `Attributes`는 컬럼, `Index`는 인덱스와 매핑됩니
> 다. 하지만 `Referential attribute`(참조 속성)는 외래 키(Foreign Key)에 해당하며, 기본 키(Primary
> Key)와는 다릅니다. 따라서 잘못된 매핑은 **"Referential attribute = Primary Key"**입니다.

---

## Question 68

Which of the below options can not be used inside an expression?

- [x] **A. The output of server action.**
- [ ] B. Both output of server action and output of data action on the screen.
- [ ] C. The output of data action on the screen.
- [ ] D. addition formula of two local integer variables present on the screen.

> **Explanation**
> The output of server action
> We can not use the output of server action directly inside an expression.
> OutSystems에서 표현식(Expression) 내에서는 서버 액션의 출력을 직접 사용할 수 없습니다. 반면,
> 데이터 액션의 출력이나 화면의 로컬 정수 변수의 연산(예: 덧셈)은 표현식에서 사용할 수 있습니
> 다.

---

## Question 69

Which is wrong in respect of buttons?

- [ ] A. We can redirect to the outside of the OutSystems application on the OnClick of button
- [ ] B. We can refresh the current screen on the Button's onClick event
- [ ] C. We can navigate to another screen on the button's onClick event.
- [x] **D. We can call a server action on the button's OnClick event**

> **Explanation**
> We can call a server action on the button's OnClick event
> Server actions can not be called on buttons on click event.
> 버튼의 `OnClick` 이벤트는 외부 URL로 리디렉션, 현재 화면 새로고침, 다른 화면으로 이동 등을
> 수행할 수 있습니다. 하지만 서버 액션을 직접 호출할 수는 없습니다(클라이언트 액션을 통해 간
> 접 호출 가능).

---

## Question 70

What will happen when we set the function property of public server action as "Yes"?

- [ ] A. It would only be defined with only one input parameter.
- [x] **B. It would only be defined with only one output parameter.**
- [ ] C. We would not be able to use this server action from another module.
- [ ] D. It would only be used inside expressions.

> **Explanation**
> It would only be defined with only one output parameter.
> 공용 서버 액션의 `Function` 속성을 `Yes`로 설정하면, 해당 액션은 표현식 편집기에서 함수처럼
> 사용할 수 있습니다. 이는 입력 및 출력 매개변수 제한을 강제하지 않으며, 다른 모듈에서도 여전
> 히 사용 가능합니다.

---

## Question 71

What is true in respect of the web blocks?

- [ ] A. An event is required to notify all the other instances about the changes made in the block.
- [ ] B. It requires an event to fire every time when there is any change in the web block to reflect it on its instance.
- [x] **C. Changes made in the web block will automatically reflect in all its instances.**
- [ ] D. The change has to be done manually on each instance of the block

> **Explanation**
> Changes made in the web block will automatically reflect in all its instances.
> 웹 블록은 재사용 가능한 구성 요소로, 블록 자체에 변경이 가해지면 모든 인스턴스에 자동으로
> 반영됩니다. 별도의 이벤트나 수동 작업이 필요 없습니다.

---

## Question 72

Regarding Blocks in OutSystems reactive apps, which of the following options is correct?

- [x] **A. Blocks can be instantiated on Screens and other Blocks**
- [ ] B. Blocks can only be instantiated on Screens
- [ ] C. Blocks can be instantiated on Screens and external HTML pages, using a special HTML tag.
- [ ] D. Blocks can be instantiated on Client Actions on the Screen.

> **Explanation**
> Blocks can be instantiated on Screens and other Blocks
> OutSystems 반응형 앱에서 블록은 화면(Screens) 및 다른 블록 내에서 인스턴스화할 수 있습니다.
> 외부 HTML 페이지나 클라이언트 액션에서는 블록을 인스턴스화할 수 없습니다.

---

## Question 73

Which of the below option is true regarding CreateOrUpdate entity action?

- [ ] A. It returns the Id only when a new record is created.
- [ ] B. It only returns Id only when NullIdentifier() in Id is passed while calling the action.
- [ ] C. It returns Id as well as a record that is updated or created.
- [x] **D. It returns only the ID of the created or updated record.**

> **Explanation**
> It returns only the ID of the created or updated record.
> `CreateOrUpdate` 엔터티 액션은 레코드가 생성되거나 업데이트될 때, 해당 레코드의 ID를 반환합
> 니다.

---

## Question 74

Which of the following is true?

- [ ] A. Aggregates and DataActions execute in the same order as they are defined on the screen.
- [ ] B. We need to call aggregates and DataAction explicitly
- [ ] C. DataAction executes before the aggregates.
- [x] **D. There is no order of aggregates and DataAction execution**

> **Explanation**
> There is no order of aggregates and DataAction execution
> 애그리게이트와 데이터 액션은 비동기적으로 실행되므로, 정의된 순서나 고정된 실행 순서가 없
> 습니다.

---

## Question 75

What is correct in respect of screen actions?

- [x] **A. All of above**
- [ ] B. Screen actions can not have output.
- [ ] C. Screen actions can not be called from outside of the screen
- [ ] D. Screen actions can not be called from client actions.

> **Explanation**
> All of above
> 화면 액션(Screen Actions)은 해당 화면 내부에서만 호출 가능하며, 외부 모듈이나 다른 화면에서
> 호출할 수 없습니다. 또한, 화면 액션(Screen Actions)은 출력 변수를 가질 수 없고, 클라이언트 액
> 션은 호출할 수 있습니다.

---
