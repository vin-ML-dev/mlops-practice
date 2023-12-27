from app import app
 
 
def test_hello():
   response = app.test_client().get('/')
   assert response.status_code == 200
   assert response.data == b'Hello world!!!'


if __name__=="__main__":
   test_hello()
