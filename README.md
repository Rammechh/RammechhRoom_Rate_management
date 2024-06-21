# Room Rate Discount API

## Overview
This is a Django project for managing room rates and discounts.

## Setup

### Prerequisites
- Python 3.x
- Django
- pip

### Installation

1. Clone the repository:
    ```sh
    git clone -b master https://github.com/Rammechh/RammechhRoom_Rate_management.git
    cd RammechhRoom_Rate_management
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the server:
    ```sh
    python manage.py runserver
    ```

6. Access the API documentation:
    - Swagger UI: `http://127.0.0.1:8000/api/swagger/`

## API Endpoints

- `GET /api/room-rates/`: Retrieve list of room rates
- `POST /api/room-rates/`: Create a new room rate
- `GET /api/room-rates/{id}/`: Retrieve a room rate by ID
- `PUT /api/room-rates/{id}/`: Update a room rate
- `DELETE /api/room-rates/{id}/`: Delete a room rate

- `GET /api/overridden-room-rates/`: Retrieve list of overridden room rates
- `POST /api/overridden-room-rates/`: Create a new overridden room rate
- `GET /api/overridden-room-rates/{id}/`: Retrieve an overridden room rate by ID
- `PUT /api/overridden-room-rates/{id}/`: Update an overridden room rate
- `DELETE /api/overridden-room-rates/{id}/`: Delete an overridden room rate

- `GET /api/discounts/`: Retrieve list of discounts
- `POST /api/discounts/`: Create a new discount
- `GET /api/discounts/{id}/`: Retrieve a discount by ID
- `PUT /api/discounts/{id}/`: Update a discount
- `DELETE /api/discounts/{id}/`: Delete a discount

- `GET /api/discount-room-rates/`: Retrieve list of discounts mapped to each room
- `POST /api/discount-room-rates/`: Create a new discount relationship for a room
- `GET /api/discount-room-rates/{id}/`: Retrieve discount relationship by ID
- `PUT /api/discount-room-rates/{id}/`: Update a discount relationship
- `DELETE /api/discount-room-rates/{id}/`: Delete a discount relationship

- `GET /api/lowest-rates/`: Retrieve the lowest rates for a given room within a date range
- 'Ex: http://127.0.0.1:8000/api/lowest-rates/?room_id=1&start_date=2024-07-01&end_date=2024-07-10
