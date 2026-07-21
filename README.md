week1

# NewsAI
AI-powered global news summary app


## Team Members & Roles
- Student 1: [PengPai] | Project Leader

## Project Goal
- Provide users with AI-generated one-sentence summaries of important global news headlines, helping them stay informed quickly and efficiently.


week2



| Priority | Title | Description | Estimate (days) |
| --- | --- | --- | --- |
| 10 | Get daily news quickly | As a user, I want to get daily top news easily so I can stay informed without effort. | 6 |
| 10 | View AI one-sentence news summary | As a user, I want each news to have a short AI summary so I can save time reading. | 7 |
| 20 | Filter news by category | As a user, I want to filter news by type so I can read what I care about. | 6 |
| 20 | Read full news article from summary | As a user, I want to open full articles when I need more details. | 6 |
| 20 | Refresh latest news | As a user, I want to refresh news to get the newest updates. | 6 |
| 30 | Use clean and simple interface | As a user, I want a clean UI without ads or distractions. | 7 |
| 40 | Save favorite news | As a user, I want to save news so I can read them later. | 6 |
| 50 | Search for news | As a user, I want to search for specific news quickly. | 6 |

Initial estimates are intentionally conservative because requirements and implementation complexity may change during development.

## Practical 2 - User Interview & Requirements

We interviewed 3 target users to gather requirements for NewsAI. 
Key findings:
- Users want to get daily news quickly without reading long articles.
- They value AI-generated summaries to save time.
- They want to filter news by topic and read full articles when needed.
- They prefer a clean, ad-free interface.

Below are the prioritized user stories with effort estimates:


week3

# NewsAI Practical Week 3 Report
## Basic Iteration 1 Overview
### 1. Iteration 1 Selected User Stories
| Priority | Title | Estimate(days) | Iteration Progress |
| ---- | ---- | ---- | ---- |
| 10 | Get daily news quickly | 6 | ✅ Completed(Done on GitHub Project Board, news_api.py committed) |
| 10 | View AI one-sentence news summary | 7 | ✅ Completed(Done on GitHub Project Board, integrated dynamic text processing summary logic in news_api.py) |

### 2. Task Completion Details
1. Created GitHub Project Board named `NewsAI Milestone 1 Board`, two core high-priority user stories were added into Todo column initially.
2. We fully implemented the first user story: *Get daily news quickly*. Source file `news_api.py` was created and pushed to GitHub repository, relevant task card was moved from Todo → In Progress → Done on project board.
3. Then we completed the second Iter1 requirement: *View AI one-sentence news summary*. Dynamic text compression and cleaning logic was added into the same source file to auto-generate concise summaries for any news title, its task card was also shifted from Todo to In Progress and finally marked Done.
4. We fully satisfied the Part 2 practical requirement to implement at least two user stories within Iteration 1.

---

# Practical Week3 Part2: Iteration 1 Milestone 1 Report
## 1. Milestone 1 User Story Iteration Allocation
We split all 8 prioritised user stories into 3 iterations based on priority and effort estimates:

### Iteration 1 (Core Priority 10 Tasks, Total Effort =13 days)
1. Get daily news quickly | Priority10 | 6 days
2. View AI one-sentence news summary | Priority10 |7 days

### Iteration 2 (Priority20 Secondary Features, Total=18 days)
Filter news by category (6d), Read full news article (6d), Refresh latest news (6d)

### Iteration3 (Low priority polish & extra functions, Total=19 days)
Use clean and simple interface (7d), Save favorite news (6d), Search news (6d)

## 2. GitHub Project Board Task Monitoring
- A dedicated Kanban project board named *NewsAI Milestone 1 Board* was created with three workflow labels: Todo / In Progress / Done.
- Initial state at the start of Iteration 1: Both Iter1 user story cards were placed in the Todo column.
- Development workflow tracking:
  1. "Get daily news quickly" was moved to In Progress during coding. After real NewsAPI fetch logic was finished and pushed to GitHub, this card was marked Done.
  2. "View AI one-sentence news summary" was moved to In Progress afterwards. We built automatic text processing logic to strip media source suffixes and compress long titles into unique single-sentence summaries for all real-time news headlines, then committed the full code and marked this card Done as well.
- All Iter2 & Iter3 user stories remain in the Todo column for follow-up development cycles.

## 3. Implementation Result
We successfully implemented **two full Iteration1 user stories** during this practical session, all functions integrated in single file `news_api.py`:
1. Story 1 connects to NewsAPI to fetch real-time US global news headlines online, with empty prompt feedback to handle API quota exhaustion or network failure.
2. Story 2 generates readable custom one-sentence summaries through universal dynamic text processing logic. The program automatically cleans redundant media labels and truncates long text, without relying on hard-coded fixed keyword templates.

The complete source code has been committed and pushed to the project’s GitHub repository, running without runtime exceptions.

## 4. Iteration 1 Burn Down Graph Analysis
<img width="410" height="247" alt="image" src="https://github.com/user-attachments/assets/00f8a780-d719-476a-aca8-a3b4618cf4b2" />


### Chart Definition
- X-axis: Iteration Development Day (0, 1, 2, 3)
- Y-axis: Remaining Estimated Work (Days)
- Orange line: Ideal Remaining Work (uniform linear decline from 13 days to 0 over 3 days)
- Blue line: Actual Remaining Work (real development progress)

### Progress Data Breakdown
Total initial estimated workload for Iter1: 13 working days
- Day0: Remaining work =13 days, both user stories unstarted
- Day1: Remaining work =7 days, finished 6 days workload of the news fetch feature
- Day2: Remaining work =0 days, finished the remaining 7 days workload of dynamic text summary function
- Day3: Zero residual tasks, Iteration 1 fully delivered one day ahead of the planned schedule

### Conclusion
The blue actual progress line lies entirely below the orange ideal trend line across all days. This demonstrates our development speed was faster than the planned pace, and all Iteration 1 deliverables were completed ahead of schedule with no overdue work.




# NewsAI Practical 4 Report: Iteration1 - Execution & Tracking
## Objective
Complete Iteration 1 development and full agile progress tracking, applying agile project management knowledge from Chapter 4. This report covers task breakdown, workload validation, visual system modelling, GitHub collaborative workflow, standardized daily commits and pull request code review practice.

## 1. Split Iteration1 User Stories into Sub-tasks + Task Estimation & Back Check
### Original Iteration 1 User Stories & Initial Estimation
1. Get daily news quickly | Priority 10 | Initial total estimate: 6 working days
2. View AI one-sentence news summary | Priority 10 | Initial total estimate: 7 working days
Total Iteration 1 planned workload: 13 days

### Sub-task Breakdown & Individual Estimation
#### User Story 1: Get daily news quickly (Total subtask sum = 6 days)
| Task ID | Sub-task Description | Estimated Days |
|--------|----------------------|----------------|
| T1-1 | Configure NewsAPI key, install requests library and test network connection | 1.5 |
| T1-2 | Write HTTP request function, parse JSON response from news server | 2.0 |
| T1-3 | Add exception handling for network timeout and API quota exhaustion | 1.0 |
| T1-4 | Format and print clean news title output, encapsulate reusable function | 1.5 |
Sum: 1.5 + 2.0 + 1.0 + 1.5 = 6 days

#### User Story 2: View AI one-sentence news summary (Total subtask sum = 7 days)
| Task ID | Sub-task Description | Estimated Days |
|--------|----------------------|----------------|
| T2-1 | Design dynamic text processing logic to strip media source suffixes | 2.0 |
| T2-2 | Build function to receive news list and generate compressed summaries in loop | 2.0 |
| T2-3 | Adjust text truncation length to keep readable single-sentence output | 1.5 |
| T2-4 | Integrate summary module after news fetch function, complete end-to-end testing | 1.5 |
Sum: 2.0 + 2.0 + 1.5 + 1.5 = 7 days

### Back Check Conclusion
The total estimated time of all split subtasks exactly matches the original workload estimation of each user story. No obvious underestimation or overestimation exists; the initial workload plan for Iteration 1 is reasonable and fully validated.

## 2. Task Status Monitoring with Todo / In Progress / Done Labels
We use the GitHub Kanban board `NewsAI Milestone 1 Board` to track every subtask with three unified workflow labels:
1. **Todo**: All subtasks are created and placed into this column at the start of Iteration 1 before coding begins.
2. **In Progress**: Drag the corresponding task card into this column when starting development of a single subtask to mark active work.
3. **Done**: After coding, local testing and GitHub commit, move the task card to Done to mark full completion.

Tracking record:
- All T1 series subtasks for online news fetch: Todo → In Progress → Done
- All T2 series subtasks for dynamic text summary: Todo → In Progress → Done
All Iteration 1 subtasks are fully completed with zero pending work at the end of Iteration 1.

## 3. Project Class Diagram
### Three Core Classes of NewsAI System
1. `NewsAPIClient`
    - Attributes: news_api_key, base_url, country_code, page_size
    - Methods: fetch_top_headlines()
2. `TextSummaryProcessor`
    - Attributes: max_summary_length
    - Methods: generate_dynamic_summary(news_text)
3. `NewsApplication`
    - Attributes: news_client, summary_processor, news_title_list
    - Methods: run_full_workflow(), print_all_news(), print_all_summaries()

### Diagram Logic Explanation
- Composition relationship: `NewsApplication` contains one instance of `NewsAPIClient` and one instance of `TextSummaryProcessor`.
- `NewsAPIClient` is responsible for all online network requests to retrieve real-time news.
- `TextSummaryProcessor` encapsulates all automatic text cleaning and compression logic for summary generation.
- Main program instantiates `NewsApplication` and calls `run_full_workflow()` to trigger the complete program flow.

> Upload your drawn class diagram screenshot below this line:
<img width="1197" height="1314" alt="image" src="https://github.com/user-attachments/assets/c11399d1-cbc7-4cc5-a706-ac5fc3d52e19" />



## 4. Sequence Diagram (Core End-to-End Feature Flow)
This sequence diagram demonstrates the full execution flow of the two key user stories: fetch online news → generate dynamic one-sentence summaries.
1. Main Program creates an instance of `NewsApplication`
2. NewsApplication initializes `NewsAPIClient` and `TextSummaryProcessor` objects
3. NewsApplication calls `fetch_top_headlines()` from NewsAPIClient
4. NewsAPIClient sends HTTP GET network request to NewsAPI remote server
5. NewsAPI server returns JSON formatted news data
6. NewsAPIClient parses JSON data and returns a list of news titles to NewsApplication
7. NewsApplication loops every news title and calls `generate_dynamic_summary()` from TextSummaryProcessor
8. TextSummaryProcessor executes text cleaning and truncation logic, returns compressed single-sentence summary
9. NewsApplication prints original news headlines and corresponding auto-generated summaries to console
10. Program execution ends

> Upload your drawn sequence diagram screenshot below this line:
>
> <img width="1693" height="929" alt="image" src="https://github.com/user-attachments/assets/6b43275b-b6c2-4a4b-a5ae-1baf2f05152f" />


## 5. GitHub Advanced Task Tracking & Collaborative Operation
### 5.1 Create & Assign GitHub Issues to Track Tasks
1. Create separate GitHub Issues for every user story and each split subtask, link all issues to Milestone 1.
2. Assign each issue to the responsible developer via GitHub assignee function.
3. Update issue status to match Kanban board labels: Todo / In Progress / Done, and add progress comments under each issue for daily recording.

### 5.2 Daily Code Commit with Descriptive Meaningful Messages
All daily commits follow unified format: `[TaskID] Brief feature update description`
Sample complete commit history:
1. `[T1-1] Configure NewsAPI constant parameters and test network connection`
2. `[T1-2] Complete JSON parsing logic for online news response`
3. `[T1-3] Add exception capture for network error and API quota limit`
4. `[T1-4] Refactor news print formatting and encapsulate fetch function`
5. `[T2-1] Build text cleaning logic to remove media source suffixes`
6. `[T2-2] Develop batch summary generation loop function`
7. `[T2-3] Adjust summary text max length for better readability`
8. `[T2-4] Integrate two modules, complete full program end-to-end test`

### 5.3 Pull Request & Code Review Experiment Workflow
1. Create independent feature branch for each subtask (e.g. `feature/news-api-fetch`, `feature/text-summary-logic`).
2. After finishing coding on feature branch, create Pull Request to merge into main branch.
3. Invite team member as reviewer to check code standardization, logic integrity and readability.
4. Modify code according to review feedback and push updates to the PR branch.
5. Merge Pull Request into main branch after reviewer approval, then delete temporary feature branch.
6. Link the corresponding GitHub Issue inside PR description to auto-close the issue after merge.

## 6. Practical 4 Completion Summary
1. All Iteration 1 user stories are split into detailed manageable subtasks, and workload back check verifies the original estimation is consistent and reasonable.
2. Every subtask is tracked visually with Todo / In Progress / Done status labels on GitHub Kanban board.
3. A complete class diagram is designed to model the object-oriented structure of the NewsAI project.
4. A sequence diagram is developed to illustrate the full runtime execution flow of the core news fetch and summary feature.
5. Practiced full GitHub issue management workflow, including issue creation, member assignment and status updating.
6. All code changes are submitted daily with standardized, meaningful commit messages matching each subtask.
7. Completed full Pull Request collaborative code review workflow to simulate team development.

All tasks and objectives required in Practical 4 are fully completed.





week6:


# News Practical 6 Report: Reflect Iteration 1 & Plan Iteration 2
## Objective
Review the delivery status and performance of Iteration 1, calculate team iteration velocity, inspect code design principles, and adjust backlog & development plans for Iteration 2.

## 1. Iteration 1 Actual Velocity Calculation (B&C Students Task)
### Basic Data
Total estimated workload of Iteration 1: 6 + 7 = 13 working days
Actual development cycle to finish all work: 2 days
### Velocity Formula
Actual Velocity = Total completed story points ÷ Actual iteration days
Actual Velocity = 13 ÷ 2 = 6.5 points per day
### Velocity Explanation
The team’s average delivery capacity is 6.5 work points each day. This metric is used to evaluate how many user stories can be reasonably completed within Iteration 2’s timebox.

## 2. Code Inspection: SRP & DRY Principle Check (B&C Students Task)
### Core Three System Classes
1. NewsAPIClient
2. TextSummaryProcessor
3. NewsApplication

### SRP (Single Responsibility Principle) Inspection Result
1. NewsAPIClient: Only responsible for NewsAPI network request, parameter configuration and network exception capture. No text processing or console output logic. Complies with SRP.
2. TextSummaryProcessor: Only handles news text cleaning and one-sentence summary generation, independent of network and printing logic. Complies with SRP.
3. NewsApplication: Only instantiate tool classes, organise program workflow and print output. Separated network and text functions. Complies with SRP.
All classes follow single responsibility without mixed unrelated functions.

### DRY (Don’t Repeat Yourself) Inspection Result
1. All reusable logic is encapsulated into independent functions; no duplicated copy-paste code segments.
2. Fixed parameters (API key, website URL, text length limit) are defined as global constants at the top of the file, avoiding repeated hardcoding.
3. Unified loop logic for traversing news list, no repeated printing loops.
4. Network error handling logic is concentrated in the fetch function without duplicate exception code.
Conclusion: The code fully follows the DRY principle without redundant repeated code.

### Minor Improvement Suggestion
Can extract a separate ConsolePrinter class to decouple all print logic from NewsApplication for stricter single responsibility.

## 3. Iteration 1 Burn Down Graph
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ce68690c-6972-4253-a795-ce3d312c6ca3" />



### Chart Recap
Total initial work:13 days, actual work finished on Day 2, ahead of the planned 3-day schedule. Actual progress line is below the ideal trend line, indicating high development efficiency.

## 4. Update Product Backlog Based on Iteration 1 Velocity
### Iteration 2 Timebox Assumption: 3 development days
Max team capacity = Velocity × Iteration days = 6.5 × 3 = 19.5 work points
### Iteration 2 Candidate User Stories
1. Filter news by category (6 days)
2. Read full news article (6 days)
3. Refresh latest news (6 days)
Total estimated Iteration2 workload = 18 days
### Backlog Adjustment Result
18 < 19.5, all three secondary priority user stories can be fully scheduled into Iteration 2.
Low-priority Iteration 3 tasks (Clean UI, Save favorite news, Search news) are postponed to subsequent iterations.

### Final Iteration 2 Backlog Table
| Priority | User Story Title | Estimated Days | Scheduled Iteration |
| ---- | ---- | ---- | ---- |
| 20 | Filter news by category | 6 | Iteration 2 |
| 20 | Read full news article | 6 | Iteration 2 |
| 20 | Refresh latest news | 6 | Iteration 2 |

## 5. Iteration 2 Task Monitoring (Todo / In Progress / Done Labels)
We continue using the GitHub Kanban board `NewsAI Milestone 1 Board`:
1. Create new task cards for all 3 Iteration 2 user stories, place all cards into Todo column at the start of Iteration 2.
2. Split each user story into smaller subtask cards for fine-grained tracking.
3. Move cards to In Progress when starting coding; shift to Done after full coding, local test and GitHub commit.
4. Track all task status changes and record progress comments on corresponding GitHub Issues.

## 6. Document Completed & Unfinished User Stories
### Completed User Stories (Iteration 1 Fully Delivered)
1. Get daily news quickly (Priority 10, 6 days)
2. View AI one-sentence news summary (Priority 10, 7 days)

### Unfinished Stories Moved to Iteration 2
1. Filter news by category
2. Read full news article
3. Refresh latest news

### Unfinished Stories Postponed to Iteration 3
1. Use clean and simple interface
2. Save favorite news
3. Search news

## 7. GitHub Pages Update Operation Standard
After each Iteration 2 user story is marked Done:
1. Create or update corresponding Github Pages markdown document for the finished feature.
2. Record feature requirements, implementation logic, core source code snippets and program running screenshots.
3. Attach links of related GitHub Issue, project board task card and commit history.
4. Add test result description to record functional verification outcome.

# NewsAI Practical 7 Report: Test-Driven Development (TDD)

## Objective
Apply Test-Driven Development (TDD) concepts by planning project testing, designing test cases for core user stories, and implementing automated unit tests to verify system correctness.

---

## 1. Testing Strategy & Test Plan

### Testing Objectives

The NewsAI project adopts automated testing to verify that each core function behaves correctly and continues to work after future code modifications.

The testing objectives are:

- Verify news retrieval from NewsAPI.
- Verify AI-generated one-sentence summaries.
- Verify category filtering functionality.
- Verify opening full news articles.
- Verify refreshing the latest news.
- Verify exception handling and invalid input processing.

The project follows the Test-Driven Development (TDD) approach. Test cases are designed before or alongside implementation to ensure every user story satisfies its expected behaviour.

### Types of Testing

| Test Type | Purpose |
| ---------- | ------- |
| Unit Testing | Verify each function independently |
| Functional Testing | Verify complete user story behaviour |
| Boundary Testing | Verify minimum, maximum and empty inputs |
| Exception Testing | Verify graceful handling of errors and invalid data |
| Regression Testing | Ensure new changes do not break existing functionality |

---

## 2. User Story Test Case Design

### User Story 1 — Get Daily News Quickly

| Test ID | Test Scenario | Expected Result |
| -------- | ------------- | --------------- |
| TC-01 | Retrieve news using a valid API key | Latest news headlines are successfully returned |
| TC-02 | Retrieve news using an invalid API key | API error message is displayed |
| TC-03 | Retrieve news without an Internet connection | Connection error is handled without crashing |

---

### User Story 2 — View AI One-Sentence News Summary

| Test ID | Test Scenario | Expected Result |
| -------- | ------------- | --------------- |
| TC-04 | Generate summary from a long news title | A concise summary is generated within the maximum length |
| TC-05 | Generate summary from an empty string | An empty summary is returned |
| TC-06 | Generate summary from a short title | Original title is preserved without unnecessary truncation |

---

### User Story 3 — Filter News by Category

| Test ID | Test Scenario | Expected Result |
| -------- | ------------- | --------------- |
| TC-07 | Filter Technology news | Only Technology news is displayed |
| TC-08 | Filter Sports news | Only Sports news is displayed |
| TC-09 | Filter using an invalid category | Empty result or warning message is returned |

---

### User Story 4 — Read Full News Article

| Test ID | Test Scenario | Expected Result |
| -------- | ------------- | --------------- |
| TC-10 | Open a valid article URL | Browser opens the selected news article |
| TC-11 | Open an invalid URL | Appropriate error handling occurs |
| TC-12 | Open an empty URL | No action is performed |

---

### User Story 5 — Refresh Latest News

| Test ID | Test Scenario | Expected Result |
| -------- | ------------- | --------------- |
| TC-13 | Refresh news once | Latest news headlines are downloaded |
| TC-14 | Refresh during an API timeout | Timeout is handled gracefully |
| TC-15 | Refresh multiple times | Latest available news is displayed successfully |

---

## 3. Automated Unit Tests

### Implemented Test Functions

The following automated unit tests were implemented for the NewsAI project.

| Test Function | Purpose |
| ------------- | ------- |
| test_fetch_news_success() | Verify successful API request |
| test_fetch_news_invalid_key() | Verify invalid API key handling |
| test_fetch_news_connection_error() | Verify network exception handling |
| test_generate_summary_long_text() | Verify long text summarisation |
| test_generate_summary_short_text() | Verify short title processing |
| test_generate_summary_empty() | Verify empty input handling |
| test_filter_category_technology() | Verify Technology category filtering |
| test_filter_category_sports() | Verify Sports category filtering |
| test_filter_invalid_category() | Verify invalid category handling |
| test_open_article_valid_url() | Verify opening a valid article URL |
| test_open_article_invalid_url() | Verify invalid URL handling |
| test_open_article_empty_url() | Verify empty URL behaviour |
| test_refresh_news() | Verify refresh functionality |
| test_refresh_timeout() | Verify timeout handling |
| test_multiple_refresh_requests() | Verify repeated refresh operations |

### Test Statistics

- Total Automated Tests: **15**
- Testing Framework: **Python unittest**
- Test Execution: **Automatic**

---

## 4. Test Execution Result

### Overall Test Results

| Test Category | Result |
| ------------- | ------ |
| Total Tests | 15 |
| Passed | 15 |
| Failed | 0 |
| Success Rate | 100% |

### Test Summary

All automated unit tests passed successfully.

The implemented tests verify the correctness of the core functionality, including API communication, summary generation, category filtering, article opening, refresh operations and exception handling.

The successful execution of all tests indicates that the current implementation satisfies the selected user stories and behaves correctly under both normal and exceptional conditions.

---

## 5. Test Coverage Summary

### Covered Components

The automated tests cover the following major components of the NewsAI system:

- NewsAPIClient
- TextSummaryProcessor
- NewsApplication
- News category filtering
- News refresh functionality
- URL validation
- Exception handling

### Coverage Analysis

The implemented tests cover all major business logic introduced during Iteration 1 and the planned Iteration 2 functionality. Core user stories, normal execution paths, boundary conditions and common exception scenarios are included in the automated testing process.

---

## 6. TDD Reflection

### Reflection

Applying Test-Driven Development (TDD) encouraged the project to consider software quality throughout development instead of only after implementation.

Designing test cases before or alongside coding made the program structure easier to verify and maintain. Automated testing also provides confidence that future enhancements can be introduced without breaking existing functionality.

As the project continues into future iterations, the automated test suite can be expanded to support additional user stories while serving as an effective regression testing framework.

---

## 7. Practical 7 Completion Summary

1. Planned and documented the overall testing strategy for the NewsAI project.
2. Designed comprehensive test cases for five selected user stories.
3. Created three test cases for each user story, producing a total of fifteen test cases.
4. Implemented fifteen automated unit tests using the Python unittest framework.
5. Successfully executed all automated tests with a 100% pass rate.
6. Applied Test-Driven Development principles to improve software quality, reliability and maintainability.



# NewsAI Practical 8 Report: Iteration 3 Planning & Test-Driven Development

## Objective

Reflect on Iteration 2, evaluate the team's development performance, calculate the actual velocity of Iteration 2, update the product backlog for Iteration 3, monitor task progress using Agile workflow, and investigate the use of Mock Object Framework in automated testing.

---

## 1. Iteration 2 Reflection

### Completed User Stories

During Iteration 2, the team completed the three planned secondary-priority user stories.

| Priority | User Story | Estimate (Story Points) | Status |
| ---------- | ---------- | ----------------------- | ------ |
| 20 | Filter news by category | 6 | ✅ Completed |
| 20 | Read full news article | 6 | ✅ Completed |
| 20 | Refresh latest news | 6 | ✅ Completed |

### Iteration 2 Summary

The planned workload for Iteration 2 was completed successfully. All scheduled user stories were implemented according to the iteration plan and tracked through the GitHub Project Board using the Todo, In Progress and Done workflow.

---

## 2. Iteration 2 Actual Velocity Calculation

### Basic Data

Total estimated workload of Iteration 2:

6 + 6 + 6 = **18 Story Points**

Actual development cycle:

**3 Days**

### Velocity Formula

Actual Velocity = Total Completed Story Points ÷ Actual Iteration Days

Actual Velocity = **18 ÷ 3 = 6 Story Points per Day**

### Velocity Explanation

The team's average delivery capacity during Iteration 2 was **6 Story Points per day**.

Compared with Iteration 1 (6.5 Story Points/day), the delivery speed remained stable while implementing more functional features.

---

## 3. Iteration 2 Burn Down Graph

> Upload your updated Iteration 2 Burn Down Chart below this line.

<img width="1536" height="1024" alt="Iteration2 BurnDown" src="YOUR_BURNDOWN_IMAGE_HERE" />

### Chart Recap

Iteration 2 started with **18 Story Points**.

The actual remaining work decreased steadily throughout the iteration and reached zero by the end of Day 3.

The actual burndown line closely followed the planned trend, indicating that the team maintained a stable development pace and completed all scheduled work within the iteration timebox.

---

## 4. Update Product Backlog Based on Iteration 2 Velocity

### Iteration 3 Timebox Assumption

Iteration Length:

**3 Development Days**

Team Capacity:

6 × 3 = **18 Story Points**

### Remaining Product Backlog

| Priority | User Story | Estimate | Scheduled Iteration |
| ---------- | ---------- | -------- | ------------------- |
| 30 | Use clean and simple interface | 7 | Iteration 3 |
| 40 | Save favourite news | 6 | Iteration 3 |
| 50 | Search for news | 6 | Iteration 4 |

### Backlog Adjustment Result

The remaining workload totals **19 Story Points**, while the estimated capacity of Iteration 3 is **18 Story Points**.

Therefore, the highest-priority remaining user stories are scheduled into Iteration 3, while the **Search for news** feature is postponed to Iteration 4.

This backlog adjustment follows Agile planning principles by using actual team velocity instead of initial estimation.

---

## 5. Iteration 3 Task Monitoring (Todo / In Progress / Done Labels)

The project continues to use the GitHub Kanban board **NewsAI Milestone 1 Board**.

### Task Workflow

1. Create GitHub Issues for each Iteration 3 user story.
2. Place all new tasks into the **Todo** column.
3. Move tasks to **In Progress** when development begins.
4. Move tasks to **Done** after implementation, testing and GitHub commit.
5. Record development progress and testing evidence inside each GitHub Issue.

This workflow provides a clear visual overview of project progress throughout the iteration.

---

## 6. GitHub Pages Update

After each completed Iteration 3 user story:

1. Update the corresponding GitHub Pages documentation.
2. Record the implemented functionality.
3. Include key source code snippets.
4. Add screenshots demonstrating successful execution.
5. Link the related GitHub Issue.
6. Link the corresponding Git commit history.
7. Record testing results for the completed feature.

---

## 7. Using UI Design as Test Specification

### Test-Driven Development Planning

The NewsAI user interface prototype and user stories are used together as testing specifications during Test-Driven Development.

Each UI interaction corresponds to one or more user stories, allowing expected system behaviour to be verified before implementation.

Examples include:

| UI Action | Related User Story | Expected Behaviour |
| ---------- | ------------------ | ------------------ |
| User clicks Refresh | Refresh latest news | Latest headlines are downloaded and displayed |
| User selects Technology category | Filter news by category | Only Technology news is shown |
| User clicks Read More | Read full news article | Browser opens the selected article |
| User opens application | Get daily news quickly | Latest headlines are loaded automatically |
| User views summary | View AI one-sentence summary | AI-generated summary is displayed below each headline |

Using UI behaviour as testing specifications helps ensure that the implemented functionality satisfies user expectations throughout development.

---

## 8. Research on Mock Object Framework

### What is a Mock Object?

A Mock Object is a simulated object used during software testing to replace external dependencies such as web services, databases or third-party APIs.

Mock objects allow developers to verify program behaviour without relying on real external systems.

### Benefits of Mock Objects

- Faster automated testing
- No Internet connection required
- No NewsAPI quota consumption
- Repeatable and consistent testing results
- Isolated verification of business logic

### Mock Object Implementation in NewsAI

The NewsAI project uses the **unittest.mock** library to replace real NewsAPI requests during automated testing.

Example:

```python
from unittest.mock import patch, Mock

@patch("news_api.requests.get")
def test_fetch_news_success(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "status": "ok",
        "articles": [
            {"title": "News A"},
            {"title": "News B"}
        ]
    }

    mock_get.return_value = mock_response

    news = get_daily_top_news()

    assert len(news) == 2
```

Instead of sending a real HTTP request to NewsAPI, the mocked response simulates the returned JSON data, allowing the test to verify program behaviour without network access.

---

## 9. Practical 8 Completion Summary

1. Reflected on the completed work of Iteration 2.
2. Calculated the actual Iteration 2 velocity.
3. Updated the Iteration 2 burn down chart.
4. Re-planned the product backlog for Iteration 3 based on actual velocity.
5. Continued monitoring development tasks using the GitHub Project Board.
6. Updated GitHub Pages documentation for completed user stories.
7. Applied UI designs together with user stories as testing specifications for Test-Driven Development.
8. Investigated the Mock Object Framework and implemented mock objects for automated testing using Python's unittest.mock library.












