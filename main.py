import pandas as pd
from pathlib import Path

# 1. Aponte para a sua pasta 'data'
pasta_principal = Path('data')

# 2. Defina o nome da pasta onde os CSVs serão salvos (pode ser qualquer nome)
pasta_destino_csv = Path('CSVs_convertidos')

# --- Início do script ---

if not pasta_principal.is_dir():
    print(f"Erro: A pasta de origem '{pasta_principal}' não foi encontrada.")
    print("Verifique se a pasta 'data' está no mesmo diretório que o script.")
else:
    print(f"Pasta de origem: '{pasta_principal}'")
    print(f"Pasta de destino: '{pasta_destino_csv}'")
    print("-" * 30)

    arquivos_excel = list(pasta_principal.rglob('*.xlsx'))

    if not arquivos_excel:
        print("Nenhum arquivo .xlsx foi encontrado dentro de 'data' e suas subpastas ('velocidade', 'fluxo').")
    else:
        print(f"{len(arquivos_excel)} arquivo(s) .xlsx encontrado(s). Iniciando conversão...")

        for arquivo_excel_origem in arquivos_excel:
            try:
                caminho_relativo = arquivo_excel_origem.relative_to(pasta_principal)
                arquivo_csv_destino = pasta_destino_csv / caminho_relativo.with_suffix('.csv')
                
                arquivo_csv_destino.parent.mkdir(parents=True, exist_ok=True)
                
                print(f"  -> Convertendo '{arquivo_excel_origem}' para '{arquivo_csv_destino}'...")

                df = pd.read_excel(arquivo_excel_origem)
                df.to_csv(arquivo_csv_destino, index=False, sep=';', encoding='utf-8-sig')

            except Exception as e:
                print(f"    !! Ocorreu um erro ao converter o arquivo {arquivo_excel_origem}: {e}")
        
        print("\nConversão concluída com sucesso!")
        print(f"Todos os arquivos CSV foram salvos em '{pasta_destino_csv}'.")