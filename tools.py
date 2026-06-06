"""
AI Analytics - AI分析工具
支持数据分析、用户分析、业务分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIAnalyticsTools:
    """
    AI分析工具
    支持：数据、用户、业务
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def analyze_data(self, data_description: str, questions: List[str]) -> Dict:
        """分析数据"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        questions_text = "\n".join(f"- {q}" for q in questions)

        prompt = f"""请分析以下数据：

数据描述：{data_description}

问题：
{questions_text}

请返回JSON格式：
{{
    "insights": ["洞察"],
    "visualizations": ["建议图表"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def analyze_user_behavior(self, behavior_data: Dict) -> Dict:
        """分析用户行为"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(behavior_data, ensure_ascii=False)

        prompt = f"""请分析以下用户行为数据：

{data_text}

请返回JSON格式：
{{
    "patterns": ["行为模式"],
    "segments": ["用户分群"],
    "opportunities": ["机会"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"user_analysis": content}

    def generate_dashboard(self, metrics: List[str], tool: str = "streamlit") -> str:
        """生成仪表板"""
        if not self.client:
            return "LLM客户端未配置"

        metrics_text = ", ".join(metrics)

        prompt = f"""请生成{tool}仪表板代码：

指标：{metrics_text}

要求：
1. 多图表布局
2. 交互筛选
3. 美观样式"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def create_funnel_analysis(self, steps: List[str], conversion_data: Dict) -> Dict:
        """创建漏斗分析"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        steps_text = " → ".join(steps)
        data_text = json.dumps(conversion_data, ensure_ascii=False)

        prompt = f"""请分析以下漏斗数据：

流程：{steps_text}
数据：{data_text}

请返回JSON格式：
{{
    "conversion_rates": {{"步骤": "转化率"}},
    "bottleneck": "瓶颈",
    "drop_off_analysis": "流失分析",
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"funnel": content}

    def generate_cohort_analysis(self, cohort_data: Dict) -> Dict:
        """创建队列分析"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(cohort_data, ensure_ascii=False)

        prompt = f"""请进行队列分析：

{data_text}

请返回JSON格式：
{{
    "retention_rates": {{}},
    "trends": ["趋势"],
    "insights": ["洞察"],
    "actions": ["行动建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cohort": content}

    def suggest_metrics(self, business_type: str, goals: List[str]) -> Dict:
        """建议指标"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        goals_text = ", ".join(goals)

        prompt = f"""请为{business_type}建议关键指标：

目标：{goals_text}

请返回JSON格式：
{{
    "north_star": "北极星指标",
    "primary_metrics": ["主要指标"],
    "secondary_metrics": ["次要指标"],
    "tracking_tools": ["推荐工具"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"metrics": content}


def create_tools(**kwargs) -> AIAnalyticsTools:
    """创建分析工具"""
    return AIAnalyticsTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Analytics Tools")
    print()

    # 测试
    metrics = tools.suggest_metrics("电商", ["提高转化", "增加复购"])
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
