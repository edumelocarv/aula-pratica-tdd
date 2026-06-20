import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

## Bug 1: calcular_media() divide por 4 fixo, em vez de len(self.notas)
def test_calcular_media_com_lista_diferente_de_4_notas():
    aluno = Aluno(nome="Pedro", notas=[10, 8, 9])
    assert aluno.calcular_media() == pytest.approx(9.0)


# Bug 2: situacao() usa "> 6.0" em vez de ">= 6.0" (média exatamente 6 deveria aprovar)
def test_situacao_aprovado_com_media_exatamente_seis():
    aluno = Aluno(nome="Ana", notas=[6, 6, 6, 6])
    assert aluno.situacao() == "Aprovado"


# Bug 3: menor_nota() chama max() em vez de min()
def test_menor_nota_retorna_a_menor_nota(aluno_aprovado):
    assert aluno_aprovado.menor_nota() == 7


# Bug 4: calcular_media_arredondada() usa int() (trunca) em vez de round()
def test_calcular_media_arredondada_deve_arredondar_nao_truncar():
    aluno = Aluno(nome="Carlos", notas=[8, 8, 8, 9])  # média = 8.25 -> deveria virar 8
    assert aluno.calcular_media_arredondada() == 8

    aluno2 = Aluno(nome="Bia", notas=[8, 8, 9, 9])  # média = 8.5 -> deveria virar 9 (truncado seria 8)
    assert aluno2.calcular_media_arredondada() == 9


# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
