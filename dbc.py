import mysql.connector as odbc
import pandas as pd

class Conexao:
    def __init__(self) -> None:
        pass

    def connection(self):
        con = odbc.connect(
           host='roundhouse.proxy.rlwy.net',
           user='root',
           password='Ef32eAF4eeB61hdAeG3E1d12dgAC4FE-',
           port='57795'
        )
        return con
        

class DataBase:
    def __init__(self):
        self.con = odbc.connect(
           host='roundhouse.proxy.rlwy.net',
           user='root',
           password='Ef32eAF4eeB61hdAeG3E1d12dgAC4FE-',
           port='57795'
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
        cursor = self.con.cursor()

        sku_exist = f"""
             select * from S3.Estoque where sku = '{sku}'  and tamanho = '{tamanho}' 
        """
        cursor.execute(sku_exist)
        exist = cursor.fetchone()

        if not(exist):    
            query = f"""
            INSERT INTO S3.Estoque (sku, produto, tipo, tamanho, quantidade)
                 VALUES('{sku}', '{produto}', '{tipo}', '{tamanho}', '{quantidade}')         
            """
            cursor.execute(query) 
            self.con.commit()
            cursor.close()
        else:
            query = f"""
                update S3.Estoque 
                set quantidade = quantidade + {quantidade} 
                where sku = '{sku}'  and tamanho = '{tamanho}' 
            """
            cursor.execute(query) 
            self.con.commit()
            cursor.close()
        

class Estoque:
    def __init__(self):
        connection = Conexao()
        self.con = connection.connection()


    def registrar_saida(self, sku, produto, tipo, tamanho, quantidade):
        query = f"""
            update S3.Estoque
            set quantidade = quantidade - {quantidade}
            where sku = '{sku}' and tamanho = '{tamanho}'
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

