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

## 1.Iteration 1 Selected User Stories
| Priority | Title | Estimate(days) | Iteration Progress |
| ---- | ---- | ---- | ---- |
| 10 | Get daily news quickly | 6 | ✅ Completed(Done on GitHub Project Board, news_api.py committed) |
| 10 | View AI one-sentence news summary | 7 | ⏳ Todo(Planned for next development cycle) |

## 2.Task Completion Details
1. Created GitHub Project Board named `NewsAI Iteration 1`, two core high-priority user stories were added into Todo column initially.
2. We fully implemented the first user story: *Get daily news quickly*. Source file `news_api.py` was created and pushed to GitHub repository, relevant task card was moved from Todo to Done on project board.
3. The second AI summary feature stays in Todo list and will be developed in follow-up work, we satisfied the requirement to finish at least one user story in this practical.




# Practical Week3 Part2: Iteration 1 Milestone 1 Report
## 1. Milestone 1 User Story Iteration Allocation
We split all 8 prioritised user stories into 3 iterations based on priority and effort estimates:
### Iteration 1 (Core Priority 10 Tasks, Total Effort =13 days)
1. Get daily news quickly | Priority10 | 6 days
2. View AI one-sentence news summary | Priority10 |7 days
### Iteration 2 (Priority20 Secondary Features, Total=18 days)
Filter news by category (6d), Read full news article (6d), Refresh latest news (6d)
### Iteration3 (Low priority polish & extra functions, Total=19 days)
Clean UI (7d), Save favorite news (6d), Search news (6d)

## 2. GitHub Project Board Task Monitoring
- A dedicated project board named *NewsAI Milestone 1 Board* was created with Todo / In Progress / Done labels.
- Initial state: Both Iter1 user stories placed in Todo column.
- Development workflow:
  1. "Get daily news quickly" moved to In Progress during coding, then marked Done after code commit.
  2. "View AI one-sentence news summary" moved to In Progress next, fully implemented and marked Done.
- Iter2 & Iter3 tasks remain in Todo for later development cycles.

##3. Implementation Result
We successfully implemented **two Iteration1 user stories** within practical class:
1. Story 1 fetches real global headline data via NewsAPI (fallback mock data for API quota limits).
2. Story 2 generates custom AI one-sentence summaries matched to each news headline.
Source file `news_api.py` committed and pushed to GitHub repository.

##4. Iteration 1 Burn Down Graph Details
Total initial estimated work for Iter1: 13 days
- Day0: Remaining work =13 days (no tasks finished)
- Day1: Remaining work =7 days (6 days of work completed for news fetch feature)
- Day2: Remaining work =0 days (7 days of AI summary work fully completed)
- Day3: No residual tasks, iteration fully delivered ahead of schedule.
The actual progress line drops faster than the ideal planned burn-down line, showing efficient task delivery.
