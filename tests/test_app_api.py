import time
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
            response = requests.post(f"{self.BASE_URL}/cars", json={"name": "Mercedes"})
            car_id = response.json()["id"]
            car = response.json()
    
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
        
    def test_delete_nonexistent_car(self):
        try:
            response = requests.delete(f"{self.BASE_URL}/cars/99999")
            assert response.status_code == 400
            assert "error" in response.json()
            assert response.json()["error"] == "Car not found"
        except Exception as e:
            print(f"An error occurred while deleting a nonexistent car: {e}")
            raise e
        
    def test_add_car_without_name(self):
        try:
            response = requests.post(f"{self.BASE_URL}/cars", json={"name": "88"})
           
            assert response.status_code == 400
            print(response.text)
            assert response.text == "Missing car name"
        except Exception as e:
            print(f"An error occurred while adding a car: {e}")
            raise e
