from manimlib.imports import *
from manim_CN import *
import os
import pyclbr
SVG_IMAGE_DIR=r'D:\app\man\ffmpeg\bin'
# 知乎_陈炳好 翻译 仅翻译注释 变量名稍作修改


class Shapes(Scene):
    #几个简单的形状
    #Python 2.7 版本。可在 Python 3.7 中直接运行，无需更改
    def construct(self):
        circle1 = Circle()
        square1 = Square()
        line1=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle1=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.play(ShowCreation(circle1))
        self.play(FadeOut(circle1))
        self.play(GrowFromCenter(square1))
        self.play(Transform(square1,triangle1))
        self.add(line1)
        self.play(FadeOut(circle1))


class MoreShapes(Scene):
    #多个简单的形状
    #2.7 版本。可在 3.7 中直接运行，无需更改
    #注：通过安装 sox 可解决报错'play command not found'
    #颜色关键字参阅manimlib\constants.py的COLOR_MAP字段，Hex色号及名称可自行修改
    #画面高度+-4 宽度+-7.1
    def construct(self):
        circle1 = Circle(color=PURPLE_A)
        square1 = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square1.move_to(UP+LEFT)
        circle1.surround(square1)
        rectangle1 = Rectangle(height=2, width=3)
        ellipse1=Ellipse(width=3, height=1, color=RED)
        ellipse1.shift(2*DOWN+2*RIGHT)
        pointer1 = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow1 = Arrow(LEFT,UP)
        arrow1.next_to(circle1,DOWN+LEFT)
        rectangle1.next_to(arrow1,DOWN+LEFT)
        ring1=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring1.next_to(ellipse1, RIGHT)

        self.add(pointer1)
        self.play(FadeIn(square1))
        self.play(Rotating(square1),FadeIn(circle1))
        self.play(GrowArrow(arrow1))
        self.play(GrowFromCenter(rectangle1), GrowFromCenter(ellipse1), GrowFromCenter(ring1))

class MovingShapes(Scene):
    #.shift 和 .move_to 的区别
    def construct(self):
        circle1=Circle(color=TEAL_A)
        circle1.move_to(LEFT)
        square1=Circle()
        square1.move_to(LEFT+3*DOWN)

        self.play(GrowFromCenter(circle1), GrowFromCenter(square1), rate=5)
        self.play(ApplyMethod(circle1.move_to,RIGHT), ApplyMethod(square1.shift,RIGHT))
        self.play(ApplyMethod(circle1.move_to,RIGHT+UP), ApplyMethod(square1.shift,RIGHT+UP))
        self.play(ApplyMethod(circle1.move_to,LEFT+UP), ApplyMethod(square1.shift,LEFT+UP))

class AddingText(Scene):
    #屏幕上显示文本
    def construct(self):
        txt1=Text("Writing with manim is fun")
        line2=Text("and easy to do!")
        line2.next_to(txt1,DOWN)
        line3=Text("for me and you!")
        line3.next_to(txt1,DOWN)

        self.add(txt1, line2)
        self.wait(2)
        self.play(Transform(line2,line3))
        self.wait(2)
        line2.shift(3*DOWN)
        self.play(ApplyMethod(txt1.shift,3*UP))
        ###尝试取消以下注释###
        #self.play(ApplyMethod(line2.move_to, LEFT_SIDE-2*LEFT))
        #self.play(ApplyMethod(txt1.next_to,line2))


class AddingMoreText(Scene):
    #使用文本属性
    def construct(self):
        txt1 = TextMobject("Imagination is more important than knowledge")
        txt1.set_color(RED)
        txt1.to_edge(UP)
        txt2 = TextMobject("A person who never made a mistake never tried anything new")
        txt2.set_color(YELLOW)
        txt3=TextMobject("-Albert Einstein")
        txt3.scale(0.75)
        txt3.next_to(txt1.get_corner(DOWN+RIGHT),DOWN)

        self.add(txt1)
        self.add(txt3)
        self.wait(2)
        self.play(Transform(txt1,txt2),ApplyMethod(txt3.move_to,txt2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(txt3.scale,1.5))
        txt3.match_color(txt2)
        self.play(FadeOut(txt1))

class RotateAndHighlight(Scene):
    #旋转文本并突出显示周围的几何图形
    def construct(self):
        square1=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        eq1=TextMobject("Text at an angle")
        eq1.bg=BackgroundRectangle(eq1,fill_opacity=1)
        eq1g=VGroup(eq1.bg,eq1)  #Order matters
        eq1g.rotate(TAU/8)
        eq2=TextMobject("Boxed text",color=BLACK)
        eq2.bg=SurroundingRectangle(eq2,color=BLUE,fill_color=RED, fill_opacity=.5)
        eq2g=VGroup(eq2,eq2.bg)
        eq2g.next_to(eq1g,DOWN)
        eq3=TextMobject("Rainbow")
        eq3.scale(2)
        eq3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        eq3.to_edge(DOWN)

        self.add(square1)
        self.play(FadeIn(eq1g))
        self.play(FadeIn(eq2g))
        self.play(FadeIn(eq3))

class BasicEquations(Scene):
    #演示如何使用Latex命令的简短脚本
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
    #方程组的分组与着色
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        help(sentence.arrange_submobjects)
        print(MED_LARGE_BUFF)
        input()
        self.play(Write(sentence))



class UsingBraces(Scene):
    #使用大括号将文本分组在一起
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eqg=VGroup(eq1A,eq2A)
        braces=Brace(eqg,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))


class UsingBracesConcise(Scene):
    #更简洁的代码块，所有列都对齐
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eqg=VGroup(eq1,eq2)
        braces=Brace(eqg,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),

    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_eq2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)



        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_eq2),ShowCreation(two_pi))


    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()


class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 2,
        "y_line_frequency" :2
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        #self.wait()

class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #创建轴和网格
        plane.add(plane.get_axis_labels())  #添加x和y标签
        self.add(plane)  #在屏幕上放置网格

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     #指向每个网格点的矢量列表

        vec_field = []  #在for循环中使用的空列表
        for point in points:
            field = 0.5*RIGHT + 0.5*UP   #向上和向右
            result = Vector(field).shift(point)   #创建矢量并将其移动到网格点
            vec_field.append(result)   #附加到列表

        draw_field = VGroup(*vec_field)   #通过向量列表创建VGroup


        self.play(ShowCreation(draw_field))   #在屏幕上绘制VGroup


class FieldWithAxes(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #在最近的提交中不起作用
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.play(ShowCreation(field))


    def calc_field(self,point):
        #这将计算单个点
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #试试这两个字段中的一个
        #efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #试试这两个字段中的一个
        return Vector(efield).shift(point)

class ExampleThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #在最近的提交中不起作用
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.set_camera_orientation(phi=PI/3,gamma=PI/5)
        self.play(ShowCreation(field2D))
        self.wait()
        #self.move_camera(gamma=0,run_time=1)   #在最近的提交中不起作用
        #self.move_camera(phi=3/4*PI, theta=-PI/2)   #在最近的提交中不起作用
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)

    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)


class EFieldInThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #在最近的提交中不起作用
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            for z in np.arange(-5,5,1)])



        self.play(ShowCreation(field3D))
        self.wait()
        #self.move_camera(0.8*np.pi/2, -0.45*np.pi)   #在最近的提交中不起作用
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def calc_field3D(self,point):
        x,y,z = point
        Rx,Ry,Rz = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)


class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #在最近的提交中不起作用
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #在最近的提交中不起作用
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001:   #Prevent divide by zero
            efield = np.array((0,0,0))  
        else:
            efield = (observation_point - source_point)/r**3
        return efield



    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)


    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration

            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())

            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3


class StickMan(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "stick_man",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.head.set_fill(self.color, opacity = 1)
        self.body.set_fill(RED, opacity = 1)
        self.arms.set_fill(YELLOW, opacity = 1)
        self.legs.set_fill(BLUE, opacity = 1)
        return self

class Waving(Scene):
    def construct(self):
        start_man = StickMan()
        plain_man = StickMan()
        waving_man = StickMan("wave")

        self.add(start_man)
        self.wait()
        self.play(Transform(start_man,waving_man))
        self.play(Transform(start_man,plain_man))

        self.wait()

class CirclesAndSquares(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "circles_and_squares",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
        "start_corner" : None,
        "circle_index" : 0,
        "line1_index" :1,
        "line2_index" : 2,
        "square1_index" : 3,
        "square2_index" : 4,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "circles_and_squares_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.circle = self.submobjects[self.circle_index]
        self.line1 = self.submobjects[self.line1_index]
        self.line2 = self.submobjects[self.line2_index]
        self.square1 = self.submobjects[self.square1_index]
        self.square2 = self.submobjects[self.square2_index]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        self.name_parts()
        self.circle.set_fill(RED, opacity = 1)
        self.line1.set_fill(self.color, opacity = 0)
        self.line2.set_fill(self.color, opacity = 0)
        self.square1.set_fill(GREEN, opacity = 1)
        self.square2.set_fill(BLUE, opacity = 1)
        return self


class SVGCircleAndSquare(Scene):
    def construct(self):
        thingy = CirclesAndSquares()

        self.add(thingy)
        self.wait()

if __name__ == "__main__":
    #在命令行调用此文件，以确保所有场景都能使用manim
    #在命令行键入 python -m manim.py P37_CN_H.py 以运行此文件中的所有场景
    #文件开头必须有 import os 和 import pyclbr 
    ###使用Python类浏览器确定此文件中定义了哪些类
    module_name = 'P37_CN_H'   #当前文件名
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim.py P37_CN_H.py %s -pl" % item.name)  #播放文件

