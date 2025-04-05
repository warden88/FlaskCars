import requests

import requests

class TestApp:
    BASE_URL = "http://127.0.0.1:5000"
    
    def test_add_car(self):
        try:
            response = requests.post(f"{self.BASE_URL}/cars", json={"name": "BMW"})
            assert response.status_code == 201
            assert response.json()["name"] == "BMW"
        except Exception as e:
            print(f"An error occurred while adding a car: {e}")
            raise e
    
    def test_get_cars(self):
        try:
            response = requests.get(f"{self.BASE_URL}/cars")
            assert response.status_code == 200
            cars = response.json()
            assert isinstance(cars, list)
        except Exception as e:
            print(f"An error occurred while fetching cars: {e}")
            raise e

    def test_delete_car(self):
        try:
            response = requests.post(f"{self.BASE_URL}/cars", json={"name": "BMW"})
            car_id = response.json()["id"]
            
            response = requests.get(f"{self.BASE_URL}/cars")
            assert response.status_code == 200
            cars = response.json()
            assert any(car["id"] == car_id for car in cars)
            
            response = requests.delete(f"{self.BASE_URL}/cars/{car_id}")
            assert response.status_code == 200
            assert response.json()["message"] == "Car deleted"

            response = requests.get(f"{self.BASE_URL}/cars")
            cars = response.json()
            assert all(car["id"] != car_id for car in cars)
        
        except Exception as e:
            print(f"An error occurred during the car deletion process: {e}")
            raise e
