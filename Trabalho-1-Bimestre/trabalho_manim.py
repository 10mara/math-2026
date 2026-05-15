from manim import *
import numpy as np

# =========================================
# HERON
# =========================================

class Heron(Scene):
    def construct(self):
        MARGEM = 0.5

        # ========== TITULO ==========
        titulo = Text(
            "Dedução da Fórmula de Heron",
            color=BLUE,
            font_size=42
        )

        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # ========== SECAO 1 ==========
        secao1 = Text(
            "1. Configuração Inicial",
            color=YELLOW,
            font_size=36
        )

        secao1.to_edge(UP, buff=MARGEM)

        self.play(Write(secao1))
        self.wait(1)

        # Triângulo
        A = np.array([-4, 1.5, 0])
        B = np.array([-6, -1, 0])
        C = np.array([-2, -1, 0])

        tri = Polygon(A, B, C, color=WHITE)

        # Labels dos vértices
        label_A = MathTex("A", font_size=28).next_to(A, UP, buff=0.1)
        label_B = MathTex("B", font_size=28).next_to(B, LEFT, buff=0.1)
        label_C = MathTex("C", font_size=28).next_to(C, RIGHT, buff=0.1)

        # Labels dos lados
        label_a = MathTex(
            "a",
            color=GREEN,
            font_size=28
        ).move_to((B + C) / 2 + DOWN * 0.3)

        label_b = MathTex(
            "b",
            color=RED,
            font_size=28
        ).move_to((A + C) / 2 + RIGHT * 0.3)

        label_c = MathTex(
            "c",
            color=BLUE,
            font_size=28
        ).move_to((A + B) / 2 + LEFT * 0.3)

        triangulo_grupo = VGroup(
            tri,
            label_A,
            label_B,
            label_C,
            label_a,
            label_b,
            label_c
        )

        self.play(Create(tri))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(2)

        explicacao1 = Text(
            "Considere um triângulo\ncom lados a, b e c.",
            font_size=26,
            line_spacing=1.2
        ).move_to([3, 1, 0])

        self.play(Write(explicacao1))
        self.wait(3)

        # Altura
        H = np.array([-4, -1, 0])

        altura = DashedLine(A, H, color=YELLOW)

        label_h = MathTex(
            "h",
            color=YELLOW,
            font_size=28
        ).next_to(altura, LEFT, buff=0.1)

        label_x = MathTex(
            "x",
            color=ORANGE,
            font_size=24
        ).move_to([-5, -1.4, 0])

        label_ax = MathTex(
            "a-x",
            color=ORANGE,
            font_size=24
        ).move_to([-3, -1.4, 0])

        self.play(Create(altura), Write(label_h))
        self.wait(1)

        self.play(Write(label_x), Write(label_ax))
        self.wait(2)

        explicacao2 = Text(
            "Traçamos a altura h\nrelativa ao lado a.",
            font_size=26,
            line_spacing=1.2
        ).move_to([3, -0.5, 0])

        self.play(FadeOut(explicacao1))
        self.play(Write(explicacao2))
        self.wait(3)

        self.play(
            FadeOut(secao1),
            FadeOut(explicacao2),
            triangulo_grupo.animate.scale(0.6).move_to([-5, 2, 0]),
            altura.animate.scale(0.6).move_to([-5, 2, 0]),
            FadeOut(label_h),
            FadeOut(label_x),
            FadeOut(label_ax)
        )

        # ========== SECAO 2 ==========
        secao2 = Text(
            "2. Aplicando Pitágoras",
            color=YELLOW,
            font_size=36
        )

        secao2.to_edge(UP, buff=MARGEM)

        self.play(Write(secao2))
        self.wait(1)

        eq_titulo = Text(
            "Nos triângulos retângulos formados:",
            font_size=26
        ).move_to([0, 1.5, 0])

        eq1 = MathTex(
            r"c^2 = h^2 + x^2",
            font_size=36
        ).move_to([0, 0.5, 0])

        eq2 = MathTex(
            r"b^2 = h^2 + (a-x)^2",
            font_size=36
        ).move_to([0, -0.3, 0])

        self.play(Write(eq_titulo))
        self.wait(1)

        self.play(Write(eq1))
        self.wait(2)

        self.play(Write(eq2))
        self.wait(3)

        explicacao3 = Text(
            "Isolando h² na 1ª equação:",
            font_size=26
        ).move_to([0, -1.2, 0])

        eq3 = MathTex(
            r"h^2 = c^2 - x^2",
            color=YELLOW,
            font_size=36
        ).move_to([0, -2, 0])

        self.play(Write(explicacao3))
        self.wait(1)

        self.play(Write(eq3))
        self.wait(3)

        self.play(
            FadeOut(eq_titulo),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(explicacao3),
            eq3.animate.move_to([0, 2, 0])
        )

        # ========== SECAO 3 ==========
        secao3 = Text(
            "3. Substituição e Simplificação",
            color=YELLOW,
            font_size=36
        )

        secao3.to_edge(UP, buff=MARGEM)

        self.play(Transform(secao2, secao3))
        self.wait(1)

        sub_texto = Text(
            "Substituindo na 2ª equação:",
            font_size=26
        ).move_to([0, 1, 0])

        eq4 = MathTex(
            r"b^2 = (c^2 - x^2) + (a-x)^2",
            font_size=34
        ).move_to([0, 0.2, 0])

        self.play(Write(sub_texto))
        self.wait(1)

        self.play(Write(eq4))
        self.wait(3)

        eq5 = MathTex(
            r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2",
            font_size=34
        ).move_to([0, -0.6, 0])

        self.play(Write(eq5))
        self.wait(2)

        eq6 = MathTex(
            r"b^2 = c^2 + a^2 - 2ax",
            font_size=34
        ).move_to([0, -1.4, 0])

        self.play(Write(eq6))
        self.wait(2)

        eq7 = MathTex(
            r"x = \frac{a^2 + c^2 - b^2}{2a}",
            color=GREEN,
            font_size=38
        ).move_to([0, -2.4, 0])

        box_x = SurroundingRectangle(eq7, color=GREEN, buff=0.15)

        self.play(Write(eq7))
        self.play(Create(box_x))
        self.wait(4)

        self.play(
            FadeOut(eq3),
            FadeOut(sub_texto),
            FadeOut(eq4),
            FadeOut(eq5),
            FadeOut(eq6),
            FadeOut(box_x),
            eq7.animate.move_to([0, 2, 0]).scale(0.8)
        )

        # ========== SECAO 4 ==========
        secao4 = Text(
            "4. Encontrando a Altura h",
            color=YELLOW,
            font_size=36
        )

        secao4.to_edge(UP, buff=MARGEM)

        self.play(Transform(secao2, secao4))
        self.wait(1)

        h_texto = Text(
            "Substituindo x em h² = c² - x²:",
            font_size=26
        ).move_to([0, 1, 0])

        self.play(Write(h_texto))
        self.wait(2)

        eq8 = MathTex(
            r"h^2 = c^2 - \left(\frac{a^2 + c^2 - b^2}{2a}\right)^2",
            font_size=32
        ).move_to([0, 0, 0])

        self.play(Write(eq8))
        self.wait(3)

        h_texto2 = Text(
            "Após simplificações algébricas:",
            font_size=26
        ).move_to([0, -1, 0])

        self.play(Write(h_texto2))
        self.wait(2)

        eq9 = MathTex(
            r"h = \frac{2\sqrt{p(p-a)(p-b)(p-c)}}{a}",
            color=ORANGE,
            font_size=34
        ).move_to([0, -2, 0])

        p_def = MathTex(
            r"\text{onde } p = \frac{a+b+c}{2}",
            font_size=28
        ).move_to([0, -2.8, 0])

        self.play(Write(eq9))
        self.wait(1)

        self.play(Write(p_def))
        self.wait(4)

        self.play(
            FadeOut(eq7),
            FadeOut(h_texto),
            FadeOut(eq8),
            FadeOut(h_texto2),
            FadeOut(p_def),
            eq9.animate.move_to([0, 1.5, 0]).scale(0.85)
        )

        # ========== SECAO 5 ==========
        secao5 = Text(
            "5. Fórmula de Heron",
            color=YELLOW,
            font_size=36
        )

        secao5.to_edge(UP, buff=MARGEM)

        self.play(Transform(secao2, secao5))
        self.wait(1)

        area_texto = Text(
            "A área do triângulo é:",
            font_size=28
        ).move_to([0, 0.5, 0])

        area_eq = MathTex(
            r"A = \frac{a \cdot h}{2}",
            font_size=36
        ).move_to([0, -0.3, 0])

        self.play(Write(area_texto))
        self.play(Write(area_eq))
        self.wait(3)

        sub_texto2 = Text(
            "Substituindo h:",
            font_size=26
        ).move_to([0, -1.1, 0])

        self.play(Write(sub_texto2))
        self.wait(1)

        area_eq2 = MathTex(
            r"A = \frac{a}{2} \cdot \frac{2\sqrt{p(p-a)(p-b)(p-c)}}{a}",
            font_size=32
        ).move_to([0, -2, 0])

        self.play(Write(area_eq2))
        self.wait(3)

        self.play(
            FadeOut(eq9),
            FadeOut(area_texto),
            FadeOut(area_eq),
            FadeOut(sub_texto2),
            FadeOut(area_eq2)
        )

        # ========== RESULTADO FINAL ==========
        final_titulo = Text(
            "FÓRMULA DE HERON",
            color=GOLD,
            font_size=42
        )

        final_titulo.to_edge(UP, buff=0.8)

        heron_formula = MathTex(
            r"A = \sqrt{p(p-a)(p-b)(p-c)}",
            font_size=52,
            color=YELLOW
        ).move_to([0, 0.3, 0])

        p_final = MathTex(
            r"p = \frac{a + b + c}{2} \text{ (semiperímetro)}",
            font_size=36
        ).move_to([0, -1, 0])

        box_final = SurroundingRectangle(
            VGroup(heron_formula, p_final),
            color=GOLD,
            buff=0.3
        )

        self.play(Transform(secao2, final_titulo))
        self.wait(1)

        self.play(Write(heron_formula))
        self.wait(1)

        self.play(Write(p_final))
        self.play(Create(box_final))
        self.wait(5)

        self.play(
            FadeOut(
                VGroup(
                    secao2,
                    heron_formula,
                    p_final,
                    box_final,
                    triangulo_grupo,
                    altura
                )
            )
        )

        self.wait(1)


# =========================================
# EXERCICIO 37 - BANDEIRA DO BRASIL
# =========================================

class Exercicio37(Scene):
    def construct(self):
        MARGEM = 0.5

        # ========== TITULO ==========
        titulo = Text(
            "Exercício 37 - Bandeira do Brasil",
            color=BLUE,
            font_size=40
        )

        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # ========== ENUNCIADO ==========
        enunciado = VGroup(
            Text(
                "Uma bandeira do Brasil tem dimensões:",
                font_size=26
            ),

            Text(
                "Retângulo: 200 cm x 140 cm",
                font_size=24
            ),

            Text(
                "Losango: diagonais 166 cm x 106 cm",
                font_size=24
            ),

            Text(
                "Círculo: raio 35 cm",
                font_size=24
            ),

            Text(
                "Qual a porcentagem da área amarela?",
                font_size=26,
                color=YELLOW
            ),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.25
        )

        enunciado.to_edge(UP, buff=MARGEM)

        self.play(Write(enunciado), run_time=3)
        self.wait(4)
        self.play(FadeOut(enunciado))

        # ========== FIGURA DA BANDEIRA ==========

        # Retângulo verde
        rect = Rectangle(
            width=4,
            height=2.8,
            color=GREEN,
            fill_opacity=0.5,
            fill_color=GREEN
        )

        # Losango amarelo
        losango = Polygon(
            [0, 1.06, 0],
            [1.66, 0, 0],
            [0, -1.06, 0],
            [-1.66, 0, 0],
            color=YELLOW,
            fill_opacity=0.7,
            fill_color=YELLOW
        )

        # Círculo azul
        circulo = Circle(
            radius=0.7,
            color=BLUE,
            fill_opacity=0.8,
            fill_color=BLUE
        )

        # Faixa branca
        faixa = Arc(
            radius=0.85,
            start_angle=-20 * DEGREES,
            angle=40 * DEGREES,
            color=WHITE,
            stroke_width=8
        )

        bandeira = VGroup(rect, losango, circulo, faixa)
        bandeira.move_to([-3.5, 0.5, 0])

        self.play(Create(rect))
        self.wait(1)

        self.play(Create(losango))
        self.wait(1)

        self.play(Create(circulo))
        self.wait(1)

        self.play(Create(faixa))
        self.wait(2)

        # ========== CALCULOS ==========

        passo1_titulo = Text(
            "1. Área do Retângulo",
            font_size=22,
            color=GREEN
        ).move_to([2.5, 2.5, 0])

        passo1_calc = MathTex(
            r"A_{\text{ret}} = 200 \times 140 = 28000 \text{ cm}^2",
            font_size=28
        ).move_to([2.5, 1.9, 0])

        self.play(Write(passo1_titulo))
        self.play(Write(passo1_calc))
        self.wait(3)

        passo2_titulo = Text(
            "2. Área do Losango",
            font_size=22,
            color=YELLOW
        ).move_to([2.5, 1.1, 0])

        passo2_calc = MathTex(
            r"A_{\text{los}} = \frac{166 \times 106}{2} = 8798 \text{ cm}^2",
            font_size=28
        ).move_to([2.5, 0.5, 0])

        self.play(Write(passo2_titulo))
        self.play(Write(passo2_calc))
        self.wait(3)

        passo3_titulo = Text(
            "3. Área do Círculo",
            font_size=22,
            color=BLUE
        ).move_to([2.5, -0.3, 0])

        passo3_calc = MathTex(
            r"A_{\text{circ}} = \frac{22}{7} \times 35^2 = 3850 \text{ cm}^2",
            font_size=28
        ).move_to([2.5, -0.9, 0])

        self.play(Write(passo3_titulo))
        self.play(Write(passo3_calc))
        self.wait(3)

        passo4_titulo = Text(
            "4. Área Amarela",
            font_size=22,
            color=ORANGE
        ).move_to([2.5, -1.7, 0])

        passo4_calc = MathTex(
            r"A_{\text{am}} = 8798 - 3850 = 4948 \text{ cm}^2",
            font_size=28
        ).move_to([2.5, -2.3, 0])

        self.play(Write(passo4_titulo))
        self.play(Write(passo4_calc))
        self.wait(3)

        calculos = VGroup(
            passo1_titulo,
            passo1_calc,
            passo2_titulo,
            passo2_calc,
            passo3_titulo,
            passo3_calc,
            passo4_titulo,
            passo4_calc
        )

        self.play(
            bandeira.animate.scale(0.5).move_to([-5, 2, 0]),
            calculos.animate.scale(0.7).move_to([0, 2, 0])
        )

        # ========== PORCENTAGEM FINAL ==========
        porcent_titulo = Text(
            "5. Porcentagem da Área Amarela",
            font_size=28,
            color=GOLD
        ).move_to([0, 0.5, 0])

        porcent_calc = MathTex(
            r"\text{Porcentagem} = \frac{A_{\text{amarela}}}{A_{\text{retângulo}}} \times 100",
            font_size=32
        ).move_to([0, -0.5, 0])

        self.play(Write(porcent_titulo))
        self.play(Write(porcent_calc))
        self.wait(2)

        porcent_sub = MathTex(
            r"= \frac{4948}{28000} \times 100",
            font_size=32
        ).move_to([0, -1.4, 0])

        self.play(Write(porcent_sub))
        self.wait(2)

        resultado = MathTex(
            r"\approx 17{,}67\%",
            font_size=56,
            color=GOLD
        ).move_to([0, -2.5, 0])

        box_resultado = SurroundingRectangle(
            resultado,
            color=GOLD,
            buff=0.2
        )

        self.play(Write(resultado))
        self.play(Create(box_resultado))
        self.wait(5)

        self.play(
            FadeOut(
                VGroup(
                    bandeira,
                    calculos,
                    porcent_titulo,
                    porcent_calc,
                    porcent_sub,
                    resultado,
                    box_resultado
                )
            )
        )

        self.wait(1)