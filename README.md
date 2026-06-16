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

