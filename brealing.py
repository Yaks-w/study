Street_dance={"breaking":"起源于1970年代的美国纽约布朗克斯区，是技巧性较高的街舞，强调舞步与动作结合。主要内容包括TopRock（站立步）、Footwork（地面步法）、Freeze（定格动作）和Power Move（力量动作），动作多样且富有挑战性，常结合体操、武术等元素",
              "Hip-Hop":"起源于1980年代末至1990年代初，是继Breaking之后流行的街舞类型。Hip-Hop注重身体协调性和上半身律动，动作幅度大而简单，适合零基础练习，强调节奏感和舞感表达"}
Street_dance["Locking"]="诞生于1960年代，由Don Cambell和The Lockers团队创立。特点是快速动作后突然定格（lock），结合手腕、手臂旋转、拍手、跳跃等动作，具有强烈的表演性和视觉冲击力"
Street_dance["Popping"]="起源于1970年代的美国西海岸，通过肌肉快速收缩与放松产生“震动”效果。Popping强调身体各部位的节奏感和机械感，常与Hip-Hop结合表演"
Street_dance["House"]="形成于1980至1990年代，融合Breaking、Hip-Hop、Salsa、Tap、Ballet等元素，以丰富轻快的脚步变化为特点。House舞可在小空间内进行，分为Jacking、Footwork和Lofting三大类"
Street_dance["Jazz"]="节奏急促、富动感，属于外放性舞蹈。Street Jazz或Jazz Funk是街舞中的爵士舞变体，强调舞感和表现力，动作自由且富有创造性"
Street_dance["Waacking"]="起源于1970年代的美国LGBTQ+社区，特点是手臂快速甩动、姿态夸张，强调表现力和个性"
Street_dance["Krump"]="由Clown舞演变而来，风格狂野夸张，通过激烈动作表达情绪和力量，强调释放内在情感"

dance=input("请输入你所查询的街舞种类")
if dance in Street_dance:
    print("你所搜索的舞种"+dance+"介绍如下")
    print(Street_dance[dance])
else:
    print("您所查询的舞种暂未收录")
    print("目前该程序收录舞种为"+str(len(Street_dance))+"个")

    # del Street_dance[....]:表示删除字典中的....