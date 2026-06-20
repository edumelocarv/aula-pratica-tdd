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

def test_contar_aprovados_todos_aprovados():
    alunos = [
        Aluno(nome="Maria", notas=[8, 9, 7, 8]),
        Aluno(nome="Lucas", notas=[7, 7, 8, 9]),
    ]
    assert contar_aprovados(alunos) == 2


def test_contar_aprovados_todos_reprovados():
    alunos = [
        Aluno(nome="João", notas=[4, 3, 5, 4]),
        Aluno(nome="Sofia", notas=[2, 3, 4, 3]),
    ]
    assert contar_aprovados(alunos) == 0


def test_contar_aprovados_lista_mista():
    alunos = [
        Aluno(nome="Maria", notas=[8, 9, 7, 8]),
        Aluno(nome="João", notas=[4, 3, 5, 4]),
    ]
    assert contar_aprovados(alunos) == 1


def test_contar_aprovados_lista_vazia():
    assert contar_aprovados([]) == 0

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função
def test_situacao_final_reprovado_por_falta_acima_de_25_porcento():
    aluno = Aluno(nome="Carlos", notas=[9, 9, 9, 9], faltas=30)
    assert aluno.situacao_final(total_aulas=100) == "Reprovado por falta"


def test_situacao_final_aprovado_com_poucas_faltas_e_media_alta():
    aluno = Aluno(nome="Maria", notas=[8, 9, 7, 8], faltas=5)
    assert aluno.situacao_final(total_aulas=100) == "Aprovado"


def test_situacao_final_reprovado_por_nota_com_poucas_faltas():
    aluno = Aluno(nome="João", notas=[4, 3, 5, 4], faltas=5)
    assert aluno.situacao_final(total_aulas=100) == "Reprovado por nota"


def test_situacao_final_com_faltas_exatamente_em_25_porcento_segue_para_media():
    aluno = Aluno(nome="Ana", notas=[8, 9, 7, 8], faltas=25)
    assert aluno.situacao_final(total_aulas=100) == "Aprovado"


def test_situacao_final_com_faltas_pouco_acima_de_25_porcento_reprova_por_falta():
    aluno = Aluno(nome="Bia", notas=[9, 9, 9, 9], faltas=26)
    assert aluno.situacao_final(total_aulas=100) == "Reprovado por falta"


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
def test_enviar_boletim_aciona_email_quando_reprovado():
    aluno = Aluno(nome="João", notas=[4, 3, 5, 4])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_called_once_with(aluno.nome, aluno.calcular_media())


def test_enviar_boletim_nao_aciona_email_quando_aprovado():
    aluno = Aluno(nome="Maria", notas=[8, 9, 7, 8])
    email_service = MagicMock()

    aluno.enviar_boletim(email_service)

    email_service.enviar.assert_not_called()
    