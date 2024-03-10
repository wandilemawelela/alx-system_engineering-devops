
# Postmortem: Load Balancer Misconfiguration Causes Authentication Service Outage

This postmortem outlines the incident where a misconfiguration in the load balancer settings resulted in an outage of the user authentication service. It provides a detailed timeline of events, identifies the root cause, describes the resolution steps taken, and outlines corrective and preventative measures to mitigate similar incidents in the future.

## Authors

- [@wandilemawelela](https://www.github.com/wandilemawelela)

## Issue Summary

* **Duration**: March 8, 2024, 10:00 AM - March 9, 2024, 2:00 AM (UTC)
* **Impact**: The user authentication service was down, resulting in users unable to log in. Approximately 30% of users were affected, experiencing login failures and service unavailability.
* **Root Cause**: The outage was caused by a misconfiguration in the load balancer settings, leading to a bottleneck in traffic distribution.

## Timeline

* **10:00 AM**: Issue detected through monitoring alerts indicating a spike in failed login attempts. Engineers observed an increase in error rates for user authentication requests.
* **10:10 AM**: Engineers investigated backend services for any anomalies, focusing on the authentication service and database servers. Initial checks showed no abnormalities.
* **11:00 AM**: Assumption made that database replication lag was causing the issue, as it could potentially delay user authentication responses. The database team was engaged to investigate further.
* **1:00 PM**: Database team confirmed that there were no significant replication delays or database issues affecting user authentication.
* **4:00 PM**: Load balancer logs were analyzed, suspecting an issue with traffic distribution. Engineers noticed uneven distribution of requests among backend servers, with some servers experiencing significantly higher loads.
* **6:00 PM**: Further analysis revealed that a recent configuration change in the load balancer settings had inadvertently skewed traffic distribution, causing certain backend servers to be overloaded while others remained underutilized.
* **8:00 PM**: Incident escalated to network infrastructure team as it became evident that the misconfiguration was within the load balancer settings.
* **12:00 AM**: Load balancer misconfiguration identified as the root cause after thorough examination of configuration files and traffic patterns.

## Root Cause and Resolution

The root cause of the outage was traced to a misconfiguration in the load balancer settings, specifically the load balancing algorithm and server weights. This misconfiguration led to uneven distribution of traffic among backend servers, resulting in overloaded servers being unable to handle authentication requests while others remained underutilized.

To resolve the issue, engineers reconfigured the load balancer to evenly distribute traffic across all backend servers using a more balanced algorithm. Additionally, server weights were adjusted to reflect the capacity of each server accurately. These changes ensured that incoming authentication requests were distributed evenly, preventing overload and improving overall system reliability.

## Corrective and Preventative Measures

To prevent similar outages in the future, the following measures will be implemented:
* Conduct regular audits of load balancer configurations to ensure proper settings and adherence to best practices.
* Enhance monitoring alerts to detect load balancer anomalies, such as uneven traffic distribution or sudden spikes in error rates.
* Implement automated tests to simulate high traffic loads on the authentication service and validate load balancer performance under various scenarios.
* Establish change management processes for load balancer configuration changes, including thorough testing and peer review before deployment.

## Tasks

* Review and update load balancer configurations to ensure uniform traffic distribution and optimal server utilization.
* Enhance monitoring system to trigger alerts for load balancer anomalies, such as skewed traffic distribution or high error rates.
* Develop automated tests to simulate high traffic loads on the authentication service and validate load balancer performance.
* Establish change management processes for load balancer configuration changes, including rigorous testing and peer review.
* Conduct training sessions for engineers on load balancer management and troubleshooting techniques to improve incident response capabilities.



