from random import randint

from pyecharts import Bar, Bar3D, EffectScatter, Line, Pie, Scatter, Scatter3D

# data=[randint(0,100) for _ in range(10000)]

def draw_pic(data,title,type_):
    title=title+'成绩分布图'
    list_1=[0,0,0,0,0]
    for i in data:
        if i>=0 and i<60:
            list_1[0]+=1
        elif i>=60 and i<70:
            list_1[1]+=1
        elif i>=70 and i<80:
            list_1[2]+=1
        elif i>=80 and i<90:
            list_1[3]+=1
        elif i>=90 and i<100:
            list_1[4]+=1
    attr=['60以下','60~70','70~80','80~90','90~100']
    if type_ == 'pie':
        pie=Pie(title=title,height=582,width=880)
        pie.use_theme('dark')
        pie.add(
            "人数",
            attr,list_1,
            is_more_utils=True,
            radius=[40,75],
            is_legend_show=True,
            is_label_show=True,
            rosetype='area'
            )
        pie.render()

    elif type_ == 'bar':
        bar=Bar(title=title,height=582,width=880)
        bar.use_theme('dark')
        bar.add(
            "人数",
            attr,
            list_1,
            is_more_utils=True,
            mark_line=['average'],
            mark_point=['min','max']
            )
        bar.render()

    elif type_ == 'bar3D' or type_ == 'bar3d':
        dot_set=[(0,0),(1,0),(2,0),(3,0),(4,0)]
        dot_set=[[x[0],x[1]] for x in dot_set]
        for i in range(5):
            dot_set[i].append(list_1[i])
        max_=1.4*max(list_1)
        range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        bar=Bar3D(title,height=582,width=880)
        # bar.use_theme('dark')
        # for x in dot_set:
        #     print(x[2])
        bar.add(
            "",
            ['低于60分','60~70','70~80','80~90','90~100'],
            [0],
            [[x[0],x[1],x[2]] for x in dot_set],
            is_visualmap=True,
            visual_range=[0, max_],
            grid3d_width=100,
            visual_range_color=range_color,
            grid3d_depth=25,
            is_more_utils=True
        )
        bar.render()


# score=[randint(0,101) for _ in range(1000)]
# data=[[i,i,randint(0,101)] for i in range(0,10001)]
# flag=[]
# dataset=[]
# for i in range(11):
#     for j in range(101):
#         if [i,j] not in flag:
#             dataset.append([i,j,randint(0,101)])

# sc=Scatter3D("",height=582,width=800)
# sc.use_theme('dark')
# range_color = [
#     '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
#     '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

# sc.add(
#     "",
#     dataset,
#     visual_range_color=range_color,
#     is_visualmap=True,
#     symbol_size=1

# )
# sc.render()
