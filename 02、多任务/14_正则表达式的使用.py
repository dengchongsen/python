# -*- coding:utf-8 -*-
import re



html = """
<div class="job-detail">
        <p>职责描述：</p><p>1.负责游戏中需求的收集和需求的分析</p><p>2.负责游戏中道具，功能，活动的文档设计和撰写，负责相关流程图设计，交互原型设计，数值设计；</p><p>3.负责跟进需求的开发，协同运营，设计，开发合作，保证版本按时发布；</p><p>4.负责把控游戏的用户体验，保证用户体验领先市场同类产品；</p><p>5.负责对已经上线的功能活动做总结，形成分析报告，并提出优化意见</p><p><br></p><p>任职要求：</p><p>1、本科学历，热爱游戏，有丰富的游戏经验，对棋牌游戏有自己的理解；</p><p>2、判断用户需求能力强，能够透过表面看到本质；</p><p>3、逻辑思维能力强，能够形成闭环；</p><p>4、具有团队精神，责任心强，抗压能力强，按时高质完成各项工作安排，跟得上版本快速迭代；</p><p>5、学习能力强，能够快速适应环境，能够在自我驱动下对自己的知识进行升级</p><p><br></p><p>成功的海外游戏制作团队邀请你一起来制作占领GOOGLE排行榜前端，玩转海外休闲棋牌游戏市场！</p>
        </div>
"""




ret = re.sub(r"<(.*?)>", '', html )

print (ret)