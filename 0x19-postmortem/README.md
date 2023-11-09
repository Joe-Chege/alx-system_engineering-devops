### Project Title: 0x19 Postmortem

#### Project Description:

This project focuses on understanding the concept of postmortems in the context of software systems. A postmortem is a detailed summary written after an outage, aimed at providing insights into the causes of the issue and ensuring preventive measures are taken.

### Task 0: My First Postmortem

#### Task Description:

Write a postmortem detailing a software outage, either real or fictional. The postmortem must adhere to the following format:

1. **Issue Summary:**
   - Duration: [Start Time - End Time (including timezone)]
   - Impact: [Describe the service affected, user experience, and percentage of users impacted]
   - Root Cause: [Explain the main cause of the issue]

2. **Timeline:**
   - Detection Time: [When the issue was first noticed]
   - Detection Method: [How the issue was detected, e.g., monitoring alert, customer complaint]
   - Actions Taken: [Steps taken to investigate the problem, initial assumptions, teams involved]
   - Misleading Paths: [Any incorrect investigation routes taken]
   - Escalation: [Teams or individuals to whom the incident was escalated]
   - Resolution: [How the incident was resolved]

3. **Root Cause and Resolution:**
   - Cause Explanation: [Detailed explanation of what caused the issue]
   - Resolution Explanation: [Detailed explanation of how the issue was fixed]

4. **Corrective and Preventative Measures:**
   - Areas for Improvement: [Broad areas that can be enhanced]
   - Specific Tasks: [List of specific tasks to address the issue, e.g., patching, adding monitoring]

Ensure the postmortem is between 400 to 600 words, clear, and concise.

### Task 1: Make People Want to Read Your Postmortem (Advanced)

#### Task Description:

Enhance your postmortem to make it engaging and attractive to readers. You can add elements such as humor, diagrams, or any creative content to catch the audience's attention.

### Additional Information:

- **Copyright:** Copyright © 2023 ALX, All rights reserved.
- **Language:** English
- **Project Dates:** Start: Nov 6, 2023, 6:00 AM - End: Nov 13, 2023, 6:00 AM
- **Review Process:** After completing the postmortem, request a manual QA review from a peer before the project deadline. If no peers are available, request a review from a TA or staff member.

### URLs:

- **GitHub Repository:** [https://github.com/Joe-Chege/alx-system_engineering-devops.git]
- **Directory:** 0x19-postmortem
- **Files:**
  - Task 0 Postmortem: [https://docs.google.com/document/d/1AjTcxXtaOnSggcctl6HY_yMoB_Ka7PGKEemPq7bEIyw/edit?usp=sharing]
  - Task 1 Postmortem Enhancement: [https://docs.google.com/document/d/1vDJMQj0JhT2ktdslzvvS7gS55Oue4MyCtRbOYi9I8Cg/edit?usp=sharing]


### Postmortem: Website Outage on November 8, 2023

#### 1. Issue Summary:

**Duration of the Outage:**  
On November 8, 2023, from 2:00 PM to 4:30 PM (UTC), our main website experienced a severe outage.

**Impact:**  
During the outage period, users were unable to access our website, resulting in a significant drop in user traffic by approximately 30%.

**Root Cause:**  
The root cause of the outage was identified as a misconfigured server update. This misconfiguration caused an unintended surge in processing demands, overwhelming the server's capacity and subsequently crashing it.

#### 2. Timeline:

**When the Issue Was Detected:**  
At 2:00 PM (UTC) on November 8, 2023, our monitoring system triggered an alert due to a sudden spike in server CPU usage.

**How the Issue Was Detected:**  
The issue was detected through our monitoring system, which identified the abnormal increase in server CPU usage, indicating a potential problem.

**Actions Taken:**  
- **System Logs Analysis:** We began by analyzing the system logs to pinpoint the source of the CPU spike.
- **Network Traffic Analysis:** Initially suspecting a DDoS attack, we analyzed network traffic patterns, but no malicious activity was found.
- **Database and Memory Investigation:** Database connections and server memory usage were investigated to rule out database-related issues, which were found to be stable.

**Misleading Investigation Paths:**  
- Initially, a network issue was suspected due to the sudden spike, but thorough analysis confirmed normal network activity.
- Database problems were considered, but stable connections and memory usage indicated otherwise.

**Escalation:**  
The incident was escalated to the DevOps team for further analysis and resolution.

**How the Incident Was Resolved:**  
The misconfigured update was identified and promptly rolled back to the previous stable configuration. Following this, the server was restarted, successfully restoring normal operations by 4:30 PM (UTC).

#### 3. Root Cause and Resolution:

**Cause Explanation:**  
The misconfigured server update inadvertently led to a significant increase in processing demands. This surge overwhelmed the server's capacity, causing it to crash and rendering the website inaccessible.

**Resolution Explanation:**  
To resolve the issue, the misconfiguration was reverted to the previous known stable settings. Subsequently, the server was restarted, ensuring that it could handle the regular processing load without any issues.

#### 4. Corrective and Preventative Measures:

**Areas for Improvement:**  
- **Deployment Procedures:** Strengthen the deployment process to prevent similar misconfigurations in the future. Implement rigorous review and testing protocols before applying updates.
- **Monitoring Enhancements:** Enhance monitoring capabilities by adding alerts for CPU and memory usage thresholds. This proactive approach will enable us to detect anomalies and potential issues before they escalate.
- **Regular Maintenance:** Schedule regular server maintenance to apply updates and patches under controlled conditions, minimizing the risk of unexpected outages.

**Specific Tasks:**  
- **Deployment Review:** Conduct a comprehensive review of the deployment procedures, involving multiple team members to ensure accuracy and prevent misconfigurations.
- **Monitoring Setup:** Implement alerts for CPU and memory usage thresholds in our monitoring system, enabling timely responses to abnormal server behavior.
- **Scheduled Maintenance:** Establish a regular maintenance schedule to apply updates during periods of low user activity, minimizing disruptions and ensuring the stability of our services.
