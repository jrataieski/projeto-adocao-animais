import json
from datetime import date

def gerar_relatorio_lotacao(cachorros, gatos):
    todos_animais = cachorros + gatos
    total_alojados = len(todos_animais)
    disponiveis = [a for a in todos_animais if a.disponibilidade]
    adotados = [a for a in todos_animais if not a.disponibilidade]

    relatorio = {
        "tipo": "Relatório de Lotação",
        "data_geracao": str(date.today()),
        "total_alojados": total_alojados,
        "total_disponiveis": len(disponiveis),
        "total_adotados": len(adotados),
        "animais_disponiveis": [
            {"codigo": a.codigo, "nome": a.nome, "especie": a.especie, "raca": a.raca} for a in disponiveis
        ]
    }

    print("\n" + "="*40)
    print("       RELATÓRIO DE LOTAÇÃO MUNICIPAL")
    print("="*40)
    print(f"Total de animais alojados: {total_alojados}")
    print(f"Aptos/Disponíveis para adoção: {len(disponiveis)}")
    print(f"Já adotados: {len(adotados)}")
    print("="*40)
    
    return relatorio

def gerar_relatorio_saude(cachorros, gatos):
    todos_animais = cachorros + gatos
    # Filtra quem não tem vacina (vacinas == False) ou não é castrado (castrado == False)
    precisam_atendimento = [a for a in todos_animais if not a.vacinas or not a.castrado]

    pendencias = []
    print("\n" + "="*40)
    print("         RELATÓRIO DE SAÚDE E PENDÊNCIAS")
    print("="*40)
    
    if not precisam_atendimento:
        print("Todos os animais estão com vacinas e castração em dia!")
    else:
        for a in precisam_atendimento:
            falta = []
            if not a.vacinas:
                falta.append("Vacina pendente")
            if not a.castrado:
                falta.append("Castração pendente")
            
            status_str = " e ".join(falta)
            print(f"[{a.codigo}] {a.nome} ({a.especie}) - {status_str}")
            
            pendencias.append({
                "codigo": a.codigo,
                "nome": a.nome,
                "especie": a.especie,
                "pendencias": status_str
            })
            
    print("="*40)

    relatorio = {
        "tipo": "Relatório de Saúde",
        "data_geracao": str(date.today()),
        "total_com_pendencias": len(pendencias),
        "animais": pendencias
    }
    return relatorio

def exportar_json(dados, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"\n[Sucesso] Relatório exportado para o arquivo '{nome_arquivo}'!")