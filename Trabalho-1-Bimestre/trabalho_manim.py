from manim import *

# =========================================
# FORMULA DE HERON 
# =========================================

class Heron(Scene):
    def construct(self):
        # Configuracao de margens seguras
        MARGEM = 0.5
        
        # ========== TITULO ==========
        titulo = Text("Deducao da Formula de Heron", color=BLUE, font_size=42)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # ========== SECAO 1: TRIANGULO E CONFIGURACAO ==========
        secao1 = Text("1. Configuracao Inicial", color=YELLOW, font_size=36)
        secao1.to_edge(UP, buff=MARGEM)
        self.play(Write(secao1))
        self.wait(1)

        # Triangulo bem posicionado a esquerda
        A = np.array([-4, 1.5, 0])
        B = np.array([-6, -1, 0])
        C = np.array([-2, -1, 0])
        
        tri = Polygon(A, B, C, color=WHITE)
        
        # Labels dos vertices
        label_A = MathTex("A", font_size=28).next_to(A, UP, buff=0.1)
        label_B = MathTex("B", font_size=28).next_to(B, LEFT, buff=0.1)
        label_C = MathTex("C", font_size=28).next_to(C, RIGHT, buff=0.1)
        
        # Labels dos lados
        label_a = MathTex("a", color=GREEN, font_size=28).move_to((B + C) / 2 + DOWN * 0.3)
        label_b = MathTex("b", color=RED, font_size=28).move_to((A + C) / 2 + RIGHT * 0.3)
        label_c = MathTex("c", color=BLUE, font_size=28).move_to((A + B) / 2 + LEFT * 0.3)
        
        triangulo_grupo = VGroup(tri, label_A, label_B, label_C, label_a, label_b, label_c)
        
        self.play(Create(tri))
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(2)

        # Explicacao a direita
        explicacao1 = Text(
            "Considere um triangulo\ncom lados a, b e c.",
            font_size=26,
            line_spacing=1.2
        ).move_to([3, 1, 0])
        self.play(Write(explicacao1))
        self.wait(3)

        # Altura h
        H = np.array([-4, -1, 0])  # Pe da altura
        altura = DashedLine(A, H, color=YELLOW)
        label_h = MathTex("h", color=YELLOW, font_size=28).next_to(altura, LEFT, buff=0.1)
        
        # Marcacao de x e (a-x)
        label_x = MathTex("x", color=ORANGE, font_size=24).move_to([-5, -1.4, 0])
        label_ax = MathTex("a-x", color=ORANGE, font_size=24).move_to([-3, -1.4, 0])
        
        self.play(Create(altura), Write(label_h))
        self.wait(1)
        self.play(Write(label_x), Write(label_ax))
        self.wait(2)

        explicacao2 = Text(
            "Tracamos a altura h\nrelativa ao lado a.",
            font_size=26,
            line_spacing=1.2
        ).move_to([3, -0.5, 0])
        self.play(FadeOut(explicacao1))
        self.play(Write(explicacao2))
        self.wait(3)

        # Limpar para proxima secao
        self.play(
            FadeOut(secao1), FadeOut(explicacao2),
            triangulo_grupo.animate.scale(0.6).move_to([-5, 2, 0]),
            altura.animate.scale(0.6).move_to([-5, 2, 0]),
            FadeOut(label_h), FadeOut(label_x), FadeOut(label_ax)
        )

        # ========== SECAO 2: TEOREMA DE PITAGORAS ==========
        secao2 = Text("2. Aplicando Pitagoras", color=YELLOW, font_size=36)
        secao2.to_edge(UP, buff=MARGEM)
        self.play(Write(secao2))
        self.wait(1)

        # Equacoes de Pitagoras
        eq_titulo = Text("Nos triangulos retangulos formados:", font_size=26)
        eq_titulo.move_to([0, 1.5, 0])
        
        eq1 = MathTex(r"c^2 = h^2 + x^2", font_size=36)
        eq1.move_to([0, 0.5, 0])
        
        eq2 = MathTex(r"b^2 = h^2 + (a-x)^2", font_size=36)
        eq2.move_to([0, -0.3, 0])
        
        self.play(Write(eq_titulo))
        self.wait(1)
        self.play(Write(eq1))
        self.wait(2)
        self.play(Write(eq2))
        self.wait(3)

        # Isolando h²
        explicacao3 = Text("Isolando h² na 1a equacao:", font_size=26)
        explicacao3.move_to([0, -1.2, 0])
        
        eq3 = MathTex(r"h^2 = c^2 - x^2", color=YELLOW, font_size=36)
        eq3.move_to([0, -2, 0])
        
        self.play(Write(explicacao3))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(3)

        # Limpar para substituicao
        self.play(
            FadeOut(eq_titulo), FadeOut(eq1), FadeOut(eq2),
            FadeOut(explicacao3),
            eq3.animate.move_to([0, 2, 0])
        )

        # ========== SECAO 3: SUBSTITUICAO ==========
        secao3 = Text("3. Substituicao e Simplificacao", color=YELLOW, font_size=36)
        secao3.to_edge(UP, buff=MARGEM)
        self.play(Transform(secao2, secao3))
        self.wait(1)

        sub_texto = Text("Substituindo na 2a equacao:", font_size=26)
        sub_texto.move_to([0, 1, 0])
        
        eq4 = MathTex(r"b^2 = (c^2 - x^2) + (a-x)^2", font_size=34)
        eq4.move_to([0, 0.2, 0])
        
        self.play(Write(sub_texto))
        self.wait(1)
        self.play(Write(eq4))
        self.wait(3)

        # Expandindo
        eq5 = MathTex(r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2", font_size=34)
        eq5.move_to([0, -0.6, 0])
        
        self.play(Write(eq5))
        self.wait(2)

        # Simplificando
        eq6 = MathTex(r"b^2 = c^2 + a^2 - 2ax", font_size=34)
        eq6.move_to([0, -1.4, 0])
        
        self.play(Write(eq6))
        self.wait(2)

        # Isolando x
        eq7 = MathTex(r"x = \frac{a^2 + c^2 - b^2}{2a}", color=GREEN, font_size=38)
        eq7.move_to([0, -2.4, 0])
        
        box_x = SurroundingRectangle(eq7, color=GREEN, buff=0.15)
        
        self.play(Write(eq7))
        self.play(Create(box_x))
        self.wait(4)

        # Limpar
        self.play(
            FadeOut(eq3), FadeOut(sub_texto), FadeOut(eq4),
            FadeOut(eq5), FadeOut(eq6), FadeOut(box_x),
            eq7.animate.move_to([0, 2, 0]).scale(0.8)
        )

        # ========== SECAO 4: ENCONTRANDO h ==========
        secao4 = Text("4. Encontrando a Altura h", color=YELLOW, font_size=36)
        secao4.to_edge(UP, buff=MARGEM)
        self.play(Transform(secao2, secao4))
        self.wait(1)

        h_texto = Text("Substituindo x em h² = c² - x²:", font_size=26)
        h_texto.move_to([0, 1, 0])
        
        self.play(Write(h_texto))
        self.wait(2)

        eq8 = MathTex(r"h^2 = c^2 - \left(\frac{a^2 + c^2 - b^2}{2a}\right)^2", font_size=32)
        eq8.move_to([0, 0, 0])
        
        self.play(Write(eq8))
        self.wait(3)

        h_texto2 = Text("Apos simplificacoes algebricas:", font_size=26)
        h_texto2.move_to([0, -1, 0])
        
        self.play(Write(h_texto2))
        self.wait(2)

        eq9 = MathTex(r"h = \frac{2\sqrt{p(p-a)(p-b)(p-c)}}{a}", color=ORANGE, font_size=34)
        eq9.move_to([0, -2, 0])
        
        p_def = MathTex(r"\text{onde } p = \frac{a+b+c}{2}", font_size=28)
        p_def.move_to([0, -2.8, 0])
        
        self.play(Write(eq9))
        self.wait(1)
        self.play(Write(p_def))
        self.wait(4)

        # Limpar
        self.play(
            FadeOut(eq7), FadeOut(h_texto), FadeOut(eq8),
            FadeOut(h_texto2), FadeOut(p_def),
            eq9.animate.move_to([0, 1.5, 0]).scale(0.85)
        )

        # ========== SECAO 5: FORMULA DE HERON ==========
        secao5 = Text("5. Formula de Heron", color=YELLOW, font_size=36)
        secao5.to_edge(UP, buff=MARGEM)
        self.play(Transform(secao2, secao5))
        self.wait(1)

        area_texto = Text("A area do triangulo e:", font_size=28)
        area_texto.move_to([0, 0.5, 0])
        
        area_eq = MathTex(r"A = \frac{a \cdot h}{2}", font_size=36)
        area_eq.move_to([0, -0.3, 0])
        
        self.play(Write(area_texto))
        self.play(Write(area_eq))
        self.wait(3)

        sub_texto2 = Text("Substituindo h:", font_size=26)
        sub_texto2.move_to([0, -1.1, 0])
        
        self.play(Write(sub_texto2))
        self.wait(1)

        area_eq2 = MathTex(
            r"A = \frac{a}{2} \cdot \frac{2\sqrt{p(p-a)(p-b)(p-c)}}{a}",
            font_size=32
        )
        area_eq2.move_to([0, -2, 0])
        
        self.play(Write(area_eq2))
        self.wait(3)

        # Limpar para resultado final
        self.play(
            FadeOut(eq9), FadeOut(area_texto), FadeOut(area_eq),
            FadeOut(sub_texto2), FadeOut(area_eq2)
        )

        # ========== RESULTADO FINAL ==========
        final_titulo = Text("FORMULA DE HERON", color=GOLD, font_size=42)
        final_titulo.to_edge(UP, buff=0.8)
        
        heron_formula = MathTex(
            r"A = \sqrt{p(p-a)(p-b)(p-c)}",
            font_size=52,
            color=YELLOW
        )
        heron_formula.move_to([0, 0.3, 0])
        
        p_final = MathTex(
            r"p = \frac{a + b + c}{2} \text{ (semiperimetro)}",
            font_size=36
        )
        p_final.move_to([0, -1, 0])
        
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

        # Fade out final
        self.play(FadeOut(VGroup(secao2, heron_formula, p_final, box_final, triangulo_grupo, altura)))
        self.wait(1)


# =========================================
# EXERCICIO 37 - BANDEIRA DO BRASIL
# =========================================

class Exercicio37(Scene):
    def construct(self):
        MARGEM = 0.5
        
        # ========== TITULO ==========
        titulo = Text("Exercicio 37 - Bandeira do Brasil", color=BLUE, font_size=40)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # ========== ENUNCIADO ==========
        enunciado = VGroup(
            Text("Uma bandeira do Brasil tem dimensoes:", font_size=26),
            Text("Retangulo: 200 cm x 140 cm", font_size=24),
            Text("Losango: diagonais 166 cm x 106 cm", font_size=24),
            Text("Circulo: raio 35 cm", font_size=24),
            Text("Qual a porcentagem da area amarela?", font_size=26, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        enunciado.to_edge(UP, buff=MARGEM)
        
        self.play(Write(enunciado), run_time=3)
        self.wait(4)
        self.play(FadeOut(enunciado))

        # ========== FIGURA DA BANDEIRA ==========
        # Retangulo verde (proporcional: 200x140 -> escala 3x2.1)
        rect = Rectangle(width=4, height=2.8, color=GREEN, fill_opacity=0.5, fill_color=GREEN)
        
        # Losango amarelo (diagonais proporcionais: 166x106 -> escala ~3.32x2.12)
        losango = Polygon(
            [0, 1.06, 0],    # topo
            [1.66, 0, 0],    # direita
            [0, -1.06, 0],   # baixo
            [-1.66, 0, 0],   # esquerda
            color=YELLOW, fill_opacity=0.7, fill_color=YELLOW
        )
        
        # Circulo azul (raio proporcional: 35 -> escala ~0.7)
        circulo = Circle(radius=0.7, color=BLUE, fill_opacity=0.8, fill_color=BLUE)
        
        bandeira = VGroup(rect, losango, circulo)
        bandeira.move_to([-3.5, 0.5, 0])
        
        self.play(Create(rect))
        self.wait(1)
        self.play(Create(losango))
        self.wait(1)
        self.play(Create(circulo))
        self.wait(2)

        # ========== CALCULOS A DIREITA ==========
        
        # Passo 1: Area do retangulo
        passo1_titulo = Text("1. Area do Retangulo (verde + losango)", font_size=22, color=GREEN)
        passo1_titulo.move_to([2.5, 2.5, 0])
        
        passo1_calc = MathTex(r"A_{\text{ret}} = 200 \times 140 = 28000 \text{ cm}^2", font_size=28)
        passo1_calc.move_to([2.5, 1.9, 0])
        
        self.play(Write(passo1_titulo))
        self.play(Write(passo1_calc))
        self.wait(3)

        # Passo 2: Area do losango
        passo2_titulo = Text("2. Area do Losango (amarelo + azul)", font_size=22, color=YELLOW)
        passo2_titulo.move_to([2.5, 1.1, 0])
        
        passo2_calc = MathTex(r"A_{\text{los}} = \frac{166 \times 106}{2} = 8798 \text{ cm}^2", font_size=28)
        passo2_calc.move_to([2.5, 0.5, 0])
        
        self.play(Write(passo2_titulo))
        self.play(Write(passo2_calc))
        self.wait(3)

        # Passo 3: Area do circulo
        passo3_titulo = Text("3. Area do Circulo (azul)", font_size=22, color=BLUE)
        passo3_titulo.move_to([2.5, -0.3, 0])
        
        passo3_calc = MathTex(r"A_{\text{circ}} = \frac{22}{7} \times 35^2 = 3850 \text{ cm}^2", font_size=28)
        passo3_calc.move_to([2.5, -0.9, 0])
        
        self.play(Write(passo3_titulo))
        self.play(Write(passo3_calc))
        self.wait(3)

        # Passo 4: Area amarela
        passo4_titulo = Text("4. Area Amarela (losango - circulo)", font_size=22, color=ORANGE)
        passo4_titulo.move_to([2.5, -1.7, 0])
        
        passo4_calc = MathTex(r"A_{\text{am}} = 8798 - 3850 = 4948 \text{ cm}^2", font_size=28)
        passo4_calc.move_to([2.5, -2.3, 0])
        
        self.play(Write(passo4_titulo))
        self.play(Write(passo4_calc))
        self.wait(3)

        # Limpar para resultado
        calculos = VGroup(
            passo1_titulo, passo1_calc,
            passo2_titulo, passo2_calc,
            passo3_titulo, passo3_calc,
            passo4_titulo, passo4_calc
        )
        
        self.play(
            bandeira.animate.scale(0.5).move_to([-5, 2, 0]),
            calculos.animate.scale(0.7).move_to([0, 2, 0])
        )

        # ========== PORCENTAGEM FINAL ==========
        porcent_titulo = Text("5. Porcentagem da Area Amarela", font_size=28, color=GOLD)
        porcent_titulo.move_to([0, 0.5, 0])
        
        porcent_calc = MathTex(
            r"\text{Porcentagem} = \frac{A_{\text{amarela}}}{A_{\text{retangulo}}} \times 100",
            font_size=32
        )
        porcent_calc.move_to([0, -0.5, 0])
        
        self.play(Write(porcent_titulo))
        self.play(Write(porcent_calc))
        self.wait(2)

        porcent_sub = MathTex(
            r"= \frac{4948}{28000} \times 100",
            font_size=32
        )
        porcent_sub.move_to([0, -1.4, 0])
        
        self.play(Write(porcent_sub))
        self.wait(2)

        # Resultado final
        resultado = MathTex(r"\approx 17{,}67\%", font_size=56, color=GOLD)
        resultado.move_to([0, -2.5, 0])
        
        box_resultado = SurroundingRectangle(resultado, color=GOLD, buff=0.2)
        
        self.play(Write(resultado))
        self.play(Create(box_resultado))
        self.wait(5)

        # Fade out
        self.play(FadeOut(VGroup(
            bandeira, calculos, porcent_titulo, porcent_calc,
            porcent_sub, resultado, box_resultado
        )))
        self.wait(1)