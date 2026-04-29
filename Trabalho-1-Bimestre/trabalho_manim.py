from manim import *

# =========================================
# 🎬 HERON COMPLETO (EXPLICADO)
# =========================================

class Heron(Scene):
    def construct(self):

        # Título
        titulo = Text("Dedução da Fórmula de Heron", color=BLUE).scale(0.8)
        self.play(Write(titulo))
        self.wait(2)
        self.play(titulo.animate.to_edge(UP))

        # Triângulo
        A = UP*2
        B = LEFT*3 + DOWN
        C = RIGHT*3 + DOWN

        tri = Polygon(A, B, C)
        self.play(Create(tri))
        self.wait(2)

        # Explicação inicial
        fala1 = Text(
            "Considere um triângulo qualquer de lados a, b e c",
            font_size=28
        ).to_edge(LEFT)
        self.play(Write(fala1))
        self.wait(4)

        # Altura
        H = [0, -1, 0]
        altura = DashedLine(A, H, color=RED)
        self.play(Create(altura))
        self.wait(2)

        fala2 = Text(
            "Traçamos a altura h relativa ao lado a",
            font_size=28
        ).next_to(fala1, DOWN)
        self.play(Write(fala2))
        self.wait(4)

        # Pitágoras
        fala3 = Text(
            "Agora aplicamos o Teorema de Pitágoras",
            font_size=28
        ).to_edge(RIGHT)
        self.play(Write(fala3))
        self.wait(3)

        eq1 = Text("c² = h² + x²", font_size=30).next_to(fala3, DOWN)
        eq2 = Text("b² = h² + (a - x)²", font_size=30).next_to(eq1, DOWN)

        self.play(Write(eq1))
        self.wait(2)
        self.play(Write(eq2))
        self.wait(5)

        # Isolar h²
        fala4 = Text(
            "Vamos isolar h² na primeira equação",
            font_size=28
        ).to_edge(LEFT)
        self.play(Transform(fala1, fala4))
        self.wait(3)

        eq3 = Text("h² = c² - x²", font_size=30, color=YELLOW)
        eq3.next_to(eq2, DOWN)

        self.play(Write(eq3))
        self.wait(5)

        # Substituição
        fala5 = Text(
            "Substituímos na segunda equação",
            font_size=28
        ).to_edge(RIGHT)
        self.play(Transform(fala3, fala5))
        self.wait(3)

        eq4 = Text("b² = c² - x² + (a - x)²", font_size=30)
        eq4.next_to(eq3, DOWN)

        self.play(Write(eq4))
        self.wait(6)

        # Resultado intermediário
        fala6 = Text(
            "Resolvendo essa expressão, encontramos x",
            font_size=28
        ).to_edge(LEFT)
        self.play(Transform(fala1, fala6))
        self.wait(3)

        eq5 = Text("x = (a² - b² + c²) / 2a", font_size=32, color=GREEN)
        eq5.to_edge(DOWN)

        self.play(Write(eq5))
        self.wait(6)

        # Área
        fala7 = Text(
            "Agora usamos a fórmula da área do triângulo",
            font_size=28
        ).to_edge(RIGHT)
        self.play(Transform(fala3, fala7))
        self.wait(3)

        area = Text("A = (a · h) / 2", font_size=32)
        area.next_to(eq5, UP)

        self.play(Write(area))
        self.wait(5)

        # Final
        fala8 = Text(
            "Após várias simplificações algébricas...",
            font_size=28
        ).to_edge(LEFT)
        self.play(Transform(fala1, fala8))
        self.wait(4)

        heron = Text(
            "A = √(p(p-a)(p-b)(p-c))",
            font_size=40,
            color=YELLOW
        )

        heron.to_edge(DOWN)

        box = SurroundingRectangle(heron, color=YELLOW)

        self.play(Write(heron))
        self.wait(2)
        self.play(Create(box))
        self.wait(6)


# =========================================
# 🎬 EXERCÍCIO 37 (EXPLICADO)
# =========================================

class Exercicio37(Scene):
    def construct(self):

        # Título
        titulo = Text("Exercício 37 - Bandeira", color=BLUE).scale(0.8)
        self.play(Write(titulo))
        self.wait(2)
        self.play(titulo.animate.to_edge(UP))

        # Retângulo
        rect = Rectangle(width=6, height=4, color=GREEN)
        self.play(Create(rect))
        self.wait(2)

        medidas = Text("200 cm x 140 cm", font_size=30)
        medidas.next_to(rect, DOWN)
        self.play(Write(medidas))
        self.wait(3)

        # Área retângulo
        fala1 = Text("Primeiro, calculamos a área total", font_size=28).to_edge(LEFT)
        self.play(Write(fala1))
        self.wait(3)

        area_rect = Text("A = 200 x 140 = 28000", font_size=30, color=GREEN)
        area_rect.next_to(fala1, DOWN)
        self.play(Write(area_rect))
        self.wait(5)

        # Losango
        losango = Polygon([0,2,0],[3,0,0],[0,-2,0],[-3,0,0], color=YELLOW)
        self.play(Create(losango))
        self.wait(3)

        fala2 = Text("Agora calculamos a área do losango", font_size=28).to_edge(LEFT)
        self.play(Transform(fala1, fala2))
        self.wait(3)

        area_losango = Text("A = (166 x 106) / 2 = 8798", font_size=30, color=YELLOW)
        area_losango.next_to(area_rect, DOWN)
        self.play(Write(area_losango))
        self.wait(5)

        # Parte verde
        fala3 = Text("Área verde = retângulo - losango", font_size=28).to_edge(LEFT)
        self.play(Transform(fala1, fala3))
        self.wait(3)

        area_verde = Text("28000 - 8798 = 19202", font_size=30, color=GREEN)
        area_verde.next_to(area_losango, DOWN)
        self.play(Write(area_verde))
        self.wait(5)

        # Círculo
        circulo = Circle(radius=1.2, color=BLUE)
        self.play(Create(circulo))
        self.wait(3)

        fala4 = Text("Agora a área do círculo azul", font_size=28).to_edge(RIGHT)
        self.play(Write(fala4))
        self.wait(3)

        area_circ = Text("A = (22/7) x 35² = 3850", font_size=30, color=BLUE)
        area_circ.next_to(fala4, DOWN)
        self.play(Write(area_circ))
        self.wait(5)

        # Parte amarela
        fala5 = Text("Área amarela = losango - círculo", font_size=28).to_edge(LEFT)
        self.play(Transform(fala1, fala5))
        self.wait(3)

        area_amarela = Text("8798 - 3850 = 4948", font_size=30, color=YELLOW)
        area_amarela.next_to(area_verde, DOWN)
        self.play(Write(area_amarela))
        self.wait(5)

        # Resultado
        fala6 = Text("Agora calculamos a porcentagem", font_size=30).to_edge(DOWN)
        self.play(Write(fala6))
        self.wait(3)

        resultado = Text("17,67%", font_size=50, color=ORANGE)
        resultado.next_to(fala6, DOWN)

        box = SurroundingRectangle(resultado, color=ORANGE)

        self.play(Write(resultado))
        self.play(Create(box))
        self.wait(6)