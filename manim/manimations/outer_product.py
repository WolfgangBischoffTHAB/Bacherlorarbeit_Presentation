from manim import *
class DefaultTemplate(MovingCameraScene):
    
    
    # CONFIG = {
        # "zoom_factor": 0.3,
        # "zoomed_display_height": 1,
        # "zoomed_display_width": 6,
        # "image_frame_stroke_width": 20,
        # "zoomed_camera_config": {
            # "default_frame_stroke_width": 3,
        # },
    # }
    
    def construct(self):
        # circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        # square = Square()  # create a square
        # square.flip(RIGHT)  # flip horizontally
        # square.rotate(-3 * TAU / 8)  # rotate a certain amount

        # self.play(Create(square))  # animate the creation of the square
        # self.play(Transform(square, circle))  # interpolate the square into the circle
        # self.play(FadeOut(square))  # fade out animation
        
        
        
        
        # rect1 = Rectangle(width=4.0, height=2.0, grid_xstep=1.0, grid_ystep=0.5)
        # rect2 = Rectangle(width=1.0, height=4.0)
        # rect3 = Rectangle(width=2.0, height=2.0, grid_xstep=1.0, grid_ystep=1.0)
        # rect3.grid_lines.set_stroke(width=1)

        # rects = Group(rect1, rect2, rect3).arrange(buff=1)
        # #self.add(rects)
        
        # #self.play(Create(rects))
        
        # self.play(Create(rect1))
        # self.play(Create(rect2))
        # self.play(Create(rect3))
        # self.wait(1)
        
        
        
        
        self.camera.frame.shift(RIGHT * 2)
        self.camera.frame.set(width=25.0)
        
        
        
        #self.scale_factor = 0.5
        #self.zoom = 0.1
        
        #self.activate_zooming(animate=False)
        #self.zoom_factor=30.0
        
        #plane = NumberPlane()
        #self.add(plane)
        
        matrixA = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self.add(matrixA)
        
        
        
        rect1 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect2 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect2.next_to(rect1, DOWN, buff=0.0)
        rect3 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect3.next_to(rect2, DOWN, buff=0.0)
        rect4 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect4.next_to(rect3, DOWN, buff=0.0)
        
        #self.add(rect1, rect2, rect3, rect4)
        
        rect_vgroup = VGroup(
            rect1,
            rect2,
            rect3,
            rect4
        )
        rect_vgroup.next_to(matrixA, RIGHT)
        self.add(rect_vgroup)
        #rect_group.scale(0.5)
        
        mac_rect = Rectangle(width=4.0, height=4.0, grid_xstep=1.0, grid_ystep=1.0)
        mac_rect.next_to(rect_vgroup, RIGHT)
        self.add(mac_rect)
        
        #self.camera.frame.set_focal_distance(10)
        #self.camera.radius = 5    # Distance from origin
        
        rect5 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect6 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect6.next_to(rect5, RIGHT, buff=0.0)
        rect7 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect7.next_to(rect6, RIGHT, buff=0.0)
        rect8 = Rectangle(width=1.0, height=1.0, grid_xstep=1.0, grid_ystep=1.0)
        rect8.next_to(rect7, RIGHT, buff=0.0)
        
        rect_vgroup2 = VGroup(
            rect5,
            rect6,
            rect7,
            rect8
        )
        
        rect_vgroup2.next_to(mac_rect, UP)
        self.add(rect_vgroup2)
        
        matrixB = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        matrixB.next_to(rect_vgroup2, UP)
        self.add(matrixB)
        
        
        
        
        matrix_a_col_0 = matrixA.get_columns()[0].copy()
        self.play(Circumscribe(matrix_a_col_0, color=RED, buff=0.2))
        sourounding_rect_a = SurroundingRectangle(matrix_a_col_0, color=RED, buff=0.1)
        matrixA.add(sourounding_rect_a)
        
        self.wait(2)
        
        matrix_b_row_0 = matrixB.get_rows()[0].copy()
        self.play(Circumscribe(matrix_b_row_0, color=BLUE, buff=0.2))
        sourounding_rect_b = SurroundingRectangle(matrix_b_row_0, color=BLUE, buff=0.1)
        matrixB.add(sourounding_rect_b)
        
        self.wait(2)
        
        
        col_A_1 = matrixA.get_rows()[0][0].copy()
        col_A_2 = matrixA.get_rows()[1][0].copy()
        col_A_3 = matrixA.get_rows()[2][0].copy()
        col_A_4 = matrixA.get_rows()[3][0].copy()
        
        col_B_1 = matrixB.get_rows()[0][0].copy()
        col_B_2 = matrixB.get_rows()[0][1].copy()
        col_B_3 = matrixB.get_rows()[0][2].copy()
        col_B_4 = matrixB.get_rows()[0][3].copy()
        
        #self.play(element.animate.shift(RIGHT*5.2).shift(UP*0.5), run_time=4) # move the copy around
        
        # self.play(col_A_1.animate.move_to(rect1.get_center()), run_time=4)
        # self.play(col_A_2.animate.move_to(rect2.get_center()), run_time=4)
        # self.play(col_A_3.animate.move_to(rect3.get_center()), run_time=4)
        # self.play(col_A_4.animate.move_to(rect4.get_center()), run_time=4)
        
        self.play(
        
            col_A_1.animate.move_to(rect1.get_center()), 
            col_A_2.animate.move_to(rect2.get_center()),
            col_A_3.animate.move_to(rect3.get_center()),
            col_A_4.animate.move_to(rect4.get_center()),
            
            col_B_1.animate.move_to(rect5.get_center()), 
            col_B_2.animate.move_to(rect6.get_center()),
            col_B_3.animate.move_to(rect7.get_center()),
            col_B_4.animate.move_to(rect8.get_center()),
            
            run_time=4)
        
        
        self.wait(4)
        
        
        
        
        
        
        #.shift(RIGHT*5.2).shift(UP*0.5)
        #.shift(UP * 1)
        
        a = col_A_1.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 1.2), run_time=2)
        text_1 = Text('1', font_size=30)
        text_1.move_to(a.get_center())
        self.add(text_1)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_2.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 2.2), run_time=2)
        text_2 = Text('5', font_size=30)
        text_2.move_to(a.get_center())
        self.add(text_2)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_3.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 3.2), run_time=2)
        text_3 = Text('9', font_size=30)
        text_3.move_to(a.get_center())
        self.add(text_3)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_4.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 4.2), run_time=2)
        text_4 = Text('13', font_size=30)
        text_4.move_to(a.get_center())
        self.add(text_4)
        self.remove(a)
        self.remove(b)

        self.wait(2)
        
        
        
        
        a = col_A_1.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 1.2), run_time=1)
        text_5 = Text('2', font_size=30)
        text_5.move_to(a.get_center())
        self.add(text_5)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 2.2), run_time=1)
        text_6 = Text('10', font_size=30)
        text_6.move_to(a.get_center())
        self.add(text_6)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 3.2), run_time=1)
        text_7 = Text('18', font_size=30)
        text_7.move_to(a.get_center())
        self.add(text_7)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 4.2), run_time=1)
        text_8 = Text('26', font_size=30)
        text_8.move_to(a.get_center())
        self.add(text_8)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        
        a = col_A_1.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 1.2), run_time=1)
        text_9 = Text('3', font_size=30)
        text_9.move_to(a.get_center())
        self.add(text_9)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 2.2), run_time=1)
        text_10 = Text('15', font_size=30)
        text_10.move_to(a.get_center())
        self.add(text_10)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 3.2), run_time=1)
        text_11 = Text('27', font_size=30)
        text_11.move_to(a.get_center())
        self.add(text_11)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 4.2), run_time=1)
        text_12 = Text('39', font_size=30)
        text_12.move_to(a.get_center())
        self.add(text_12)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        
        
        a = col_A_1.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 1.2), run_time=1)
        text_13 = Text('4', font_size=30)
        text_13.move_to(a.get_center())
        self.add(text_13)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 2.2), run_time=1)
        text_14 = Text('20', font_size=30)
        text_14.move_to(a.get_center())
        self.add(text_14)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 3.2), run_time=1)
        text_15 = Text('36', font_size=30)
        text_15.move_to(a.get_center())
        self.add(text_15)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 4.2), run_time=1)
        text_16 = Text('52', font_size=30)
        text_16.move_to(a.get_center())
        self.add(text_16)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        
        self.wait(2.0)
        
        matrixA.remove(sourounding_rect_a)
        matrixB.remove(sourounding_rect_b)
        
        self.remove(col_A_1)
        self.remove(col_A_2)
        self.remove(col_A_3)
        self.remove(col_A_4)
        
        self.remove(col_B_1)
        self.remove(col_B_2)
        self.remove(col_B_3)
        self.remove(col_B_4)
        
        self.wait(2.0)
        
        
        
        
        
        
        
        matrix_a_col_0 = matrixA.get_columns()[1].copy()
        self.play(Circumscribe(matrix_a_col_0, color=RED, buff=0.2))
        matrixA.remove(sourounding_rect_a)
        sourounding_rect_a = SurroundingRectangle(matrix_a_col_0, color=RED, buff=0.1)
        matrixA.add(sourounding_rect_a)
        
        self.wait(2)
        
        matrix_b_row_0 = matrixB.get_rows()[1].copy()
        self.play(Circumscribe(matrix_b_row_0, color=BLUE, buff=0.2))
        matrixB.remove(sourounding_rect_b)
        sourounding_rect_b = SurroundingRectangle(matrix_b_row_0, color=BLUE, buff=0.1)
        matrixB.add(sourounding_rect_b)
        
        self.wait(2)
        
        
        self.wait(2.0)        
        
        col_A_1 = matrixA.get_rows()[0][1].copy()
        col_A_2 = matrixA.get_rows()[1][1].copy()
        col_A_3 = matrixA.get_rows()[2][1].copy()
        col_A_4 = matrixA.get_rows()[3][1].copy()
        
        col_B_1 = matrixB.get_rows()[1][0].copy()
        col_B_2 = matrixB.get_rows()[1][1].copy()
        col_B_3 = matrixB.get_rows()[1][2].copy()
        col_B_4 = matrixB.get_rows()[1][3].copy()
        
        #self.play(element.animate.shift(RIGHT*5.2).shift(UP*0.5), run_time=4) # move the copy around
        
        # self.play(col_A_1.animate.move_to(rect1.get_center()), run_time=4)
        # self.play(col_A_2.animate.move_to(rect2.get_center()), run_time=4)
        # self.play(col_A_3.animate.move_to(rect3.get_center()), run_time=4)
        # self.play(col_A_4.animate.move_to(rect4.get_center()), run_time=4)
        
        self.play(
        
            col_A_1.animate.move_to(rect1.get_center()), 
            col_A_2.animate.move_to(rect2.get_center()),
            col_A_3.animate.move_to(rect3.get_center()),
            col_A_4.animate.move_to(rect4.get_center()),
            
            col_B_1.animate.move_to(rect5.get_center()), 
            col_B_2.animate.move_to(rect6.get_center()),
            col_B_3.animate.move_to(rect7.get_center()),
            col_B_4.animate.move_to(rect8.get_center()),
            
            run_time=4)
        
        
        self.wait(4)
        
        
        
        
        a = col_A_1.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 1.2), run_time=2)
        self.remove(text_1)
        text_1 = Text('11', font_size=30)
        text_1.move_to(a.get_center())
        self.add(text_1)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_2.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 2.2), run_time=2)
        self.remove(text_2)
        text_2 = Text('35', font_size=30)
        text_2.move_to(a.get_center())
        self.add(text_2)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_3.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 3.2), run_time=2)
        self.remove(text_3)
        text_3 = Text('59', font_size=30)
        text_3.move_to(a.get_center())
        self.add(text_3)
        self.remove(a)
        self.remove(b)
        
        self.wait(1)
        
        a = col_A_4.copy()
        b = col_B_1.copy()
        self.play(a.animate.shift(RIGHT * 1.2), b.animate.shift(DOWN * 4.2), run_time=2)
        self.remove(text_4)
        text_4 = Text('83', font_size=30)
        text_4.move_to(a.get_center())
        self.add(text_4)
        self.remove(a)
        self.remove(b)

        self.wait(2)
        
        
        
        
        
        
        a = col_A_1.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 1.2), run_time=1)
        self.remove(text_5)
        text_5 = Text('14', font_size=30)
        text_5.move_to(a.get_center())
        self.add(text_5)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 2.2), run_time=1)
        self.remove(text_6)
        text_6 = Text('46', font_size=30)
        text_6.move_to(a.get_center())
        self.add(text_6)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 3.2), run_time=1)
        self.remove(text_7)
        text_7 = Text('78', font_size=30)
        text_7.move_to(a.get_center())
        self.add(text_7)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_2.copy()
        self.play(a.animate.shift(RIGHT * 2.2), b.animate.shift(DOWN * 4.2), run_time=1)
        self.remove(text_8)
        text_8 = Text('110', font_size=30)
        text_8.move_to(a.get_center())
        self.add(text_8)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        
        a = col_A_1.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 1.2), run_time=1)
        self.remove(text_9)
        text_9 = Text('17', font_size=30)
        text_9.move_to(a.get_center())
        self.add(text_9)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 2.2), run_time=1)
        self.remove(text_10)
        text_10 = Text('57', font_size=30)
        text_10.move_to(a.get_center())
        self.add(text_10)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 3.2), run_time=1)
        self.remove(text_11)
        text_11 = Text('97', font_size=30)
        text_11.move_to(a.get_center())
        self.add(text_11)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_3.copy()
        self.play(a.animate.shift(RIGHT * 3.2), b.animate.shift(DOWN * 4.2), run_time=1)
        self.remove(text_12)
        text_12 = Text('137', font_size=30)
        text_12.move_to(a.get_center())
        self.add(text_12)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        
        
        a = col_A_1.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 1.2), run_time=1)
        self.remove(text_13)
        text_13 = Text('20', font_size=30)
        text_13.move_to(a.get_center())
        self.add(text_13)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_2.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 2.2), run_time=1)
        self.remove(text_14)
        text_14 = Text('68', font_size=30)
        text_14.move_to(a.get_center())
        self.add(text_14)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_3.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 3.2), run_time=1)
        self.remove(text_15)
        text_15 = Text('116', font_size=30)
        text_15.move_to(a.get_center())
        self.add(text_15)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        a = col_A_4.copy()
        b = col_B_4.copy()
        self.play(a.animate.shift(RIGHT * 4.2), b.animate.shift(DOWN * 4.2), run_time=1)
        self.remove(text_16)
        text_16 = Text('164', font_size=30)
        text_16.move_to(a.get_center())
        self.add(text_16)
        self.remove(a)
        self.remove(b)
        
        self.wait(0.1)
        
        
        
        
        self.wait(4)
        
        #Group(matrixA, rect1).arrange(buff=1)
        
        #rect1_first_cell = rect1[0]
        
        
        
        
        
        # rect2 = Rectangle(width=1.0, height=1.0, grid_xstep=4.0, grid_ystep=1.0)
        # matrixB = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        
        # rectsA = Group(matrixA, rect1).arrange(buff=1)
        # rectsB = Group(matrixB, rect2).arrange(buff=1)
        
        # rectsAll = Group(rectsA).arrange(buff=1)
        # #rectsAll = Group(rectsA, rectsB).arrange(buff=1)
        
        
        # self.add(rectsAll)
        
        
        
        # self.wait(1)
        
        
        # #self.play(TransformInStages.from_copy(group, tex3[0],      lag_ratio=0.4, run_time=2.5))
        
        # #element = matrixA.get_rows()[1].copy() # copy a row from the matrix
        # element = matrixA.get_rows()[0][0].copy()
        # #self.play(element.animate.shift(RIGHT*3.2).shift(UP*1.3), run_time=4) # move the copy around
        
        # #self.play(element.animate.move_to(rect1_first_cell.get_top()))
        # #dot = always_redraw(lambda : element.move_to(rect1.get_center()))
        
        # self.wait(2)



        # circle = Circle()
        # square = Square()
        # triangle = Triangle()

        # circle.shift(LEFT)
        # square.shift(UP)
        # triangle.shift(RIGHT)

        # self.add(circle, square, triangle)
        # self.wait(1)
        
        
        
        # self.play(Create(circle))
        # self.play(Create(square))
        # self.play(Create(triangle))
        # self.wait()
        
        
        
        # plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()
        # box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7, fill_color = RED_B, fill_opacity = 0.5, height=1, width=1)

        # dot = always_redraw(lambda : Dot().move_to(box.get_center()))

        # # code = Code("Tute1Code1.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
        # # tab_width = 2, line_spacing = 0.3, scale_factor = 0.5, font="Monospace").set_width(6).to_edge(UL, buff=0)

        # # self.play(FadeIn(plane), Write(code), run_time = 6)
        # # self.wait()
        # self.add(box, dot)
        # self.play(box.animate.shift(RIGHT*2), run_time=4)
        # self.wait()
        # self.play(box.animate.shift(UP*3), run_time=4)
        # self.wait()
        # self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=4)
        # self.wait()
        # self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=4)
        # self.wait()
        
        
        
        
        
        # plane = NumberPlane(x_range=[-7,7,1], y_range=[-4,4,1]).add_coordinates()

        # axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], x_length = 6, y_length=6)
        # axes.to_edge(LEFT, buff=0.5)
        
        # circle = Circle(stroke_width = 6, stroke_color = YELLOW, fill_color = RED_C, fill_opacity = 0.8)
        # circle.set_width(2).to_edge(DR, buff=0)

        # triangle = Triangle(stroke_color = ORANGE, stroke_width = 10, 
        # fill_color = GREY).set_height(2).shift(DOWN*3+RIGHT*3)

        # # code = Code("Tute1Code2.py", style=Code.styles_list[12], background ="window", language = "python", insert_line_no = True,
            # # tab_width = 2, line_spacing = 0.3, scale_factor = 0.5, font="Monospace").set_width(8).to_edge(UR, buff=0)

        # # self.play(FadeIn(plane), Write(code), run_time=6)
        # # self.wait()
        # self.play(Write(axes))
        # self.wait()
        # self.play(plane.animate.set_opacity(0.4))
        # self.wait()
        # self.play(DrawBorderThenFill(circle))
        # self.wait()
        # self.play(circle.animate.set_width(1))
        # self.wait()
        # self.play(Transform(circle, triangle), run_time=3)
        # self.wait()
        
        
        
        
        # y0, y1 = Term("y", subscript=0), Term("y", subscript=1)
        # x0, x1 = Term("x", subscript=0), Term("x", subscript=1)

        # tex1 = MathTex(y0, "=", w00, x0, "+", w01, x1)
        # self.add(tex1)
        
        # self.wait()