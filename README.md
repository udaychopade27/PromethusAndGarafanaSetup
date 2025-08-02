# 📈 Prometheus & Grafana Monitoring Stack with Docker

This project sets up a complete monitoring and alerting stack using **Prometheus**, **Grafana**, **Alertmanager**, **Node Exporter**, **Blackbox Exporter**, **cAdvisor**, **Loki**, and **Promtail** – all orchestrated using **Docker Compose**.

## 🚀 Stack Overview

- **Prometheus** – Core metrics collection & alerting engine
- **Grafana** – Visualization and dashboarding
- **Alertmanager** – Notification system (email alerts)
- **Node Exporter** – OS-level metrics
- **Blackbox Exporter** – Website uptime checks
- **cAdvisor** – Docker container metrics
- **Loki + Promtail** – Log aggregation and monitoring

## 📂 Folder Structure
```text .
├── docker-compose.yml
├── prometheus.yml
├── grafana/ # Datasource provisioning
├── rules/ # Prometheus rule files
│ ├── prometheus.rules.yml
│ └── alerting.rules.yml
├── alertmanager/
│ └── alertmanager.yml
├── blackbox/
│ └── monitor_website.yml
├── loki/
│ ├── loki-config.yml
│ └── promtail-config.yml
```
---

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/udaychopade27/PromethusAndGarafanaSetup.git
cd PromethusAndGarafanaSetup
```
2. **Start the stack**
```bash
   docker-compose up -d
```
3. **Access UI Dashboards**
```text .
| Service           | URL                                            |
| ----------------- | ---------------------------------------------- |
| Prometheus        | [http://localhost:9090](http://localhost:9090) |
| Grafana           | [http://localhost:3000](http://localhost:3000) |
| Alertmanager      | [http://localhost:9093](http://localhost:9093) |
| Blackbox Exporter | [http://localhost:9115](http://localhost:9115) |
| cAdvisor          | [http://localhost:8081](http://localhost:8081) |
```
---
Default Grafana Login: **admin / admin**
---

## 📬 Alerting

Prometheus triggers alerts (e.g., if a target is down), and Alertmanager sends email notifications. Update alertmanager.yml with your valid email settings.

---

## 📦 Metrics Collected
* System resource metrics from node-exporter
* Container metrics from cAdvisor
* Website uptime from blackbox-exporter
* Log files from Promtail + Loki
  
---

## 📊 Dashboards
- Import prebuilt dashboards for:
- Docker Monitoring
- Node Exporter Full
- Blackbox Uptime
- Loki Logs
  
---

## 📌 Future Enhancements
- Add TLS & OAuth for Grafana
- Create custom recording rules
- Set up Slack notifications
- Integrate with Kubernetes

---

## 👨‍💻 Author
**Uday Chopade**
- 🔗 [portfolio](https://udaychopade27.lovable.app)
- ✍️ [Linkedin](https://www.linkedin.com/in/udaychopade27)
- 🐙 [GitHub](https://www.github.com/udaychopade27)

