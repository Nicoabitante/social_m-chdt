# Social Media App

### Requirements 
- Docker compose:  [install](https://docs.docker.com/compose/install/)

### Run Application
- clone repository
  ```
    git clone https://github.com/Nicoabitante/social_m-chdt.git
  ```
- go to the application directory
   ```
        cd social_m-chdt
   ```
- execute docker compose
    
  ``` docker compose up ```

### Run tests
     docker exec -ti social_m_chdt-web-1  poetry run pytest
