from manim import *
class DefaultTemplate(MovingCameraScene):
    
    def move_add_vector(self, idx, matrixC):
        self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        self.wait(1)
        matrix_a_col_0 = matrixA.get_columns()[idx][0].copy()
        matrix_b_col_0 = matrixB.get_columns()[idx][0].copy()
        matrix_a_col_0.set_color(RED)
        matrix_b_col_0.set_color(RED)
        self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        self.remove(matrix_a_col_0, matrix_b_col_0)
        rect_vgroup.remove(matrixC)
        #matrixC = Matrix([[2, 4, 6, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        matrixC.next_to(matrixB, DOWN, buff=0.3)
        rect_vgroup.add(matrixC)
    
    def construct(self):
        
        #self.camera.frame.shift(LEFT * 6)
        #self.camera.frame.shift(DOWN * 2)
        self.camera.frame.set(width=20.0)
        
        aluRect = Rectangle(width=10.0, height=3.5, grid_xstep=0.0, grid_ystep=0.0)
        self.add(aluRect)
        
        matrixA = Matrix([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]])
        
        self.add(matrixA)
        
        matrixB = Matrix([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]])
        matrixB.next_to(matrixA, DOWN, buff=0.3)
        self.add(matrixB)
        
        matrixC = Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        matrixC.next_to(matrixB, DOWN, buff=0.3)
        self.add(matrixC)
        
        rect_vgroup = VGroup(
            matrixA,
            matrixB,
            matrixC
        )
        
        #matrixC.next_to(matrixB, DOWN)
        #self.add(matrixC)
        
        rect_vgroup.next_to(aluRect, RIGHT)
        self.add(rect_vgroup)
        
        self.wait(2)
        
        
        
        
        self.play(rect_vgroup.animate.shift(LEFT * 10.5))        
        self.wait(1)
        matrix_a_col_0 = matrixA.get_columns()[0][0].copy()
        matrix_b_col_0 = matrixB.get_columns()[0][0].copy()
        matrix_a_col_1 = matrixA.get_columns()[1][0].copy()
        matrix_b_col_1 = matrixB.get_columns()[1][0].copy()
        matrix_a_col_2 = matrixA.get_columns()[2][0].copy()
        matrix_b_col_2 = matrixB.get_columns()[2][0].copy()
        matrix_a_col_3 = matrixA.get_columns()[3][0].copy()
        matrix_b_col_3 = matrixB.get_columns()[3][0].copy()
        matrix_a_col_4 = matrixA.get_columns()[4][0].copy()
        matrix_b_col_4 = matrixB.get_columns()[4][0].copy()
        matrix_a_col_5 = matrixA.get_columns()[5][0].copy()
        matrix_b_col_5 = matrixB.get_columns()[5][0].copy()
        matrix_a_col_6 = matrixA.get_columns()[6][0].copy()
        matrix_b_col_6 = matrixB.get_columns()[6][0].copy()
        matrix_a_col_7 = matrixA.get_columns()[7][0].copy()
        matrix_b_col_7 = matrixB.get_columns()[7][0].copy()
        matrix_a_col_0.set_color(RED)
        matrix_b_col_0.set_color(RED)
        matrix_a_col_1.set_color(RED)
        matrix_b_col_1.set_color(RED)
        matrix_a_col_2.set_color(RED)
        matrix_b_col_2.set_color(RED)
        matrix_a_col_3.set_color(RED)
        matrix_b_col_3.set_color(RED)
        matrix_a_col_4.set_color(RED)
        matrix_b_col_4.set_color(RED)
        matrix_a_col_5.set_color(RED)
        matrix_b_col_5.set_color(RED)
        matrix_a_col_6.set_color(RED)
        matrix_b_col_6.set_color(RED)
        matrix_a_col_7.set_color(RED)
        matrix_b_col_7.set_color(RED)
        self.play(
            matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75),
            matrix_a_col_1.animate.scale(1.75), matrix_b_col_1.animate.scale(1.75),
            matrix_a_col_2.animate.scale(1.75), matrix_b_col_2.animate.scale(1.75),
            matrix_a_col_3.animate.scale(1.75), matrix_b_col_3.animate.scale(1.75),
            matrix_a_col_4.animate.scale(1.75), matrix_b_col_4.animate.scale(1.75),
            matrix_a_col_5.animate.scale(1.75), matrix_b_col_5.animate.scale(1.75),
            matrix_a_col_6.animate.scale(1.75), matrix_b_col_6.animate.scale(1.75),
            matrix_a_col_7.animate.scale(1.75), matrix_b_col_7.animate.scale(1.75)
        )
        self.play(
            matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2),
            matrix_a_col_1.animate.shift(DOWN * 2.4), matrix_b_col_1.animate.shift(DOWN * 1.2),
            matrix_a_col_2.animate.shift(DOWN * 2.4), matrix_b_col_2.animate.shift(DOWN * 1.2),
            matrix_a_col_3.animate.shift(DOWN * 2.4), matrix_b_col_3.animate.shift(DOWN * 1.2),
            matrix_a_col_4.animate.shift(DOWN * 2.4), matrix_b_col_4.animate.shift(DOWN * 1.2),
            matrix_a_col_5.animate.shift(DOWN * 2.4), matrix_b_col_5.animate.shift(DOWN * 1.2),
            matrix_a_col_6.animate.shift(DOWN * 2.4), matrix_b_col_6.animate.shift(DOWN * 1.2),
            matrix_a_col_7.animate.shift(DOWN * 2.4), matrix_b_col_7.animate.shift(DOWN * 1.2)
        )
        self.remove(
            matrix_a_col_0, matrix_b_col_0,
            matrix_a_col_1, matrix_b_col_1,
            matrix_a_col_2, matrix_b_col_2,
            matrix_a_col_3, matrix_b_col_3,
            matrix_a_col_4, matrix_b_col_4,
            matrix_a_col_5, matrix_b_col_5,
            matrix_a_col_6, matrix_b_col_6,
            matrix_a_col_7, matrix_b_col_7
        )
        rect_vgroup.remove(matrixC)
        matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        matrixC.next_to(matrixB, DOWN, buff=0.3)
        rect_vgroup.add(matrixC)
        
        self.wait(2)
        
        self.play(rect_vgroup.animate.shift(LEFT * 10))        
        self.wait(1)
        matrix_a_col_0 = matrixA.get_columns()[8][0].copy()
        matrix_b_col_0 = matrixB.get_columns()[8][0].copy()
        matrix_a_col_1 = matrixA.get_columns()[9][0].copy()
        matrix_b_col_1 = matrixB.get_columns()[9][0].copy()
        matrix_a_col_2 = matrixA.get_columns()[10][0].copy()
        matrix_b_col_2 = matrixB.get_columns()[10][0].copy()
        matrix_a_col_3 = matrixA.get_columns()[11][0].copy()
        matrix_b_col_3 = matrixB.get_columns()[11][0].copy()
        matrix_a_col_4 = matrixA.get_columns()[12][0].copy()
        matrix_b_col_4 = matrixB.get_columns()[12][0].copy()
        matrix_a_col_5 = matrixA.get_columns()[13][0].copy()
        matrix_b_col_5 = matrixB.get_columns()[13][0].copy()
        matrix_a_col_6 = matrixA.get_columns()[14][0].copy()
        matrix_b_col_6 = matrixB.get_columns()[14][0].copy()
        matrix_a_col_7 = matrixA.get_columns()[15][0].copy()
        matrix_b_col_7 = matrixB.get_columns()[15][0].copy()
        matrix_a_col_0.set_color(RED)
        matrix_b_col_0.set_color(RED)
        matrix_a_col_1.set_color(RED)
        matrix_b_col_1.set_color(RED)
        matrix_a_col_2.set_color(RED)
        matrix_b_col_2.set_color(RED)
        matrix_a_col_3.set_color(RED)
        matrix_b_col_3.set_color(RED)
        matrix_a_col_4.set_color(RED)
        matrix_b_col_4.set_color(RED)
        matrix_a_col_5.set_color(RED)
        matrix_b_col_5.set_color(RED)
        matrix_a_col_6.set_color(RED)
        matrix_b_col_6.set_color(RED)
        matrix_a_col_7.set_color(RED)
        matrix_b_col_7.set_color(RED)
        self.play(
            matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75),
            matrix_a_col_1.animate.scale(1.75), matrix_b_col_1.animate.scale(1.75),
            matrix_a_col_2.animate.scale(1.75), matrix_b_col_2.animate.scale(1.75),
            matrix_a_col_3.animate.scale(1.75), matrix_b_col_3.animate.scale(1.75),
            matrix_a_col_4.animate.scale(1.75), matrix_b_col_4.animate.scale(1.75),
            matrix_a_col_5.animate.scale(1.75), matrix_b_col_5.animate.scale(1.75),
            matrix_a_col_6.animate.scale(1.75), matrix_b_col_6.animate.scale(1.75),
            matrix_a_col_7.animate.scale(1.75), matrix_b_col_7.animate.scale(1.75)
        )
        self.play(
            matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2),
            matrix_a_col_1.animate.shift(DOWN * 2.4), matrix_b_col_1.animate.shift(DOWN * 1.2),
            matrix_a_col_2.animate.shift(DOWN * 2.4), matrix_b_col_2.animate.shift(DOWN * 1.2),
            matrix_a_col_3.animate.shift(DOWN * 2.4), matrix_b_col_3.animate.shift(DOWN * 1.2),
            matrix_a_col_4.animate.shift(DOWN * 2.4), matrix_b_col_4.animate.shift(DOWN * 1.2),
            matrix_a_col_5.animate.shift(DOWN * 2.4), matrix_b_col_5.animate.shift(DOWN * 1.2),
            matrix_a_col_6.animate.shift(DOWN * 2.4), matrix_b_col_6.animate.shift(DOWN * 1.2),
            matrix_a_col_7.animate.shift(DOWN * 2.4), matrix_b_col_7.animate.shift(DOWN * 1.2)
        )
        self.remove(
            matrix_a_col_0, matrix_b_col_0,
            matrix_a_col_1, matrix_b_col_1,
            matrix_a_col_2, matrix_b_col_2,
            matrix_a_col_3, matrix_b_col_3,
            matrix_a_col_4, matrix_b_col_4,
            matrix_a_col_5, matrix_b_col_5,
            matrix_a_col_6, matrix_b_col_6,
            matrix_a_col_7, matrix_b_col_7
        )
        rect_vgroup.remove(matrixC)
        matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 ]])
        matrixC.next_to(matrixB, DOWN, buff=0.3)
        rect_vgroup.add(matrixC)
        
        self.wait(2)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[1][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[1][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[2][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[2][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[3][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[3][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[4][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[4][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[5][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[5][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[6][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[6][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[7][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[7][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 0, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[8][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[8][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[9][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[9][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 0, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[10][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[10][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 0, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[11][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[11][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 0, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[12][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[12][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 0, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[13][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[13][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 0, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[14][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[14][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 0 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)
        
        # self.play(rect_vgroup.animate.shift(LEFT * 1.28))        
        # self.wait(1)
        # matrix_a_col_0 = matrixA.get_columns()[15][0].copy()
        # matrix_b_col_0 = matrixB.get_columns()[15][0].copy()
        # matrix_a_col_0.set_color(RED)
        # matrix_b_col_0.set_color(RED)
        # self.play(matrix_a_col_0.animate.scale(1.75), matrix_b_col_0.animate.scale(1.75))
        # self.play(matrix_a_col_0.animate.shift(DOWN * 2.4), matrix_b_col_0.animate.shift(DOWN * 1.2))
        # self.remove(matrix_a_col_0, matrix_b_col_0)
        # rect_vgroup.remove(matrixC)
        # matrixC = Matrix([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 ]])
        # matrixC.next_to(matrixB, DOWN, buff=0.3)
        # rect_vgroup.add(matrixC)