import mysql.connector as odbc
import pandas as pd
import jsonify 

class DataBase:
    def __init__(self):
        self.con = odbc.connect(
           host='containers-us-west-114.railway.app',
           user='root',
           password='Sq5fg8cBpkMOAgSYChMq',
           port='7626'
        )

    
    def cadastrar_fornecedor(self, nome, logradouro, numero, 
                             complemento, bairro, municipio, uf, cep, telefone, email):
        
        query = f"""
        INSERT INTO S3.Fornecedor(nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email)
                 VALUES('{nome}', '{logradouro}', '{numero}', '{complemento}', '{bairro}', '{municipio}', '{uf}', '{cep}', '{telefone}', '{email}')         
        """
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        cursor.close()

        

    def cadastrar_produto(self, sku, fornecedor, tipo, produto, custo, preco_venda):
        query = f"""
        INSERT INTO S3.Produtos (sku, fornecedor, tipo, produto, custo, preco_venda)
                 VALUES('{sku}', '{fornecedor}', '{tipo}', '{produto}', '{custo}', '{ preco_venda}')         
        """
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        cursor.close()

    def pesquisa_sku(self, sku):
        query = f"""
        select * from S3.Produtos where sku = '{sku}'
        """

        cursor = self.con.cursor()
        cursor.execute(query)
        resultado = cursor.fetchone()
        print(resultado)
        return resultado
        #return jsonify(resultado)
        
    def registrar_entrada(self, sku, produto, tipo, tamanho, quantidade):
        query = f"""
        INSERT INTO S3.Estoque (sku, produto, tipo, tamanho, quantidade)
                 VALUES('{sku}', '{produto}', '{tipo}', '{tamanho}', '{quantidade}')         
        """
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        cursor.close()





# con = odbc.connect(
#             host='localhost',
#             database='world',
#             user='root',
#             password='@Wess-3705',
#             auth_plugin='mysql_native_password'
#         ) 
# cursor = con.cursor()
# query = """
#     INSERT INTO fornecedor.empresas(nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email)
#                  VALUES('wsley', 'teste', 'vndcia', '26541', 'ncianc', 'mcopamopc', 'cjbaujcdb', 'cjbziub', 'vcnokasn', 'cnaondc')   
#         """
# cursor.execute(query)
# con.commit()

