# 📊 AI Analytics

AI分析工具，支持数据分析、用户分析、业务分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📊 数据分析
- 👤 用户行为分析
- 📈 仪表板生成
- 🔄 漏斗分析
- 👥 队列分析
- 📏 指标建议

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_analytics import create_tools

tools = create_tools()

# 数据分析
analysis = tools.analyze_data("销售数据", ["趋势", "异常"])

# 用户行为
user = tools.analyze_user_behavior(behavior_data)

# 仪表板
dashboard = tools.generate_dashboard(["DAU", "转化率", "ARPU"])

# 漏斗分析
funnel = tools.create_funnel_analysis(steps, conversion_data)

# 队列分析
cohort = tools.generate_cohort_analysis(cohort_data)

# 指标建议
metrics = tools.suggest_metrics("电商", ["提高转化"])
```

## 📁 项目结构

```
ai-analytics/
├── tools.py       # 分析工具核心
└── README.md
```

## 📄 许可证

MIT License
