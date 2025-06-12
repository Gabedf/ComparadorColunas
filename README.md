
# Comparador de Nomes entre Duas Colunas de Arquivo Excel

Este projeto é uma ferramenta simples de visualização e comparação entre duas colunas de um arquivo `.xlsx`. Ele identifica os nomes que estão na **Coluna A**, mas não estão presentes na **Coluna B**, e salva esses nomes em um arquivo de texto chamado `nomes_faltantes.txt`.

## 🔧 Funcionalidades

- Interface visual para seleção de arquivo Excel.
- Leitura das colunas especificadas (COLUNA A e COLUNA B).
- Comparação dos nomes linha a linha.
- Geração automática de um relatório com os nomes faltantes.
- Abertura automática do relatório ao final da execução.

## 📁 Estrutura

```
main.py                 # Script principal que executa a comparação
requirements.txt        # Arquivos com dependências do projeto
visuals/
  └── visual.py         # Contém a interface para seleção de arquivos
```

## ▶️ Como Usar

1. **Instale as dependências** (de preferência dentro de um ambiente virtual):

```bash
pip install -r requirements.txt
```

2. **Execute o programa principal:**

```bash
python main.py
```

3. **Selecione o arquivo `.xlsx`** contendo as colunas `COLUNA A` e `COLUNA B`.

4. O programa criará e abrirá automaticamente o arquivo `nomes_faltantes.txt` com os nomes exclusivos da Coluna A.

## ✅ Requisitos

- Python 3.10+
- Estrutura do Excel com as colunas nomeadas como `COLUNA A` e `COLUNA B`.

## 🧪 Dependências

As bibliotecas utilizadas estão listadas em `requirements.txt`:

- pandas
- openpyxl
- numpy
- python-dateutil
- pytz
- six
- tzdata
- et_xmlfile

## 📝 Licença

Este projeto é de uso livre para fins educacionais ou profissionais.
