#!/bin/bash

# Zatrzymaj wszystkie działające kontenery
echo "Zatrzymywanie wszystkich kontenerów..."
docker stop $(docker ps -aq)

# Usuń wszystkie kontenery (działające i zatrzymane)
echo "Usuwanie wszystkich kontenerów..."
docker rm $(docker ps -aq)

# Usuń wszystkie obrazy Docker
echo "Usuwanie wszystkich obrazów Docker..."
docker rmi $(docker images -q)

# Usuń wszystkie woluminy Docker
echo "Usuwanie wszystkich woluminów Docker..."
docker volume rm $(docker volume ls -q)

# Usuń wszystkie sieci Docker
echo "Usuwanie wszystkich sieci Docker..."
docker network rm $(docker network ls -q)

# Opcjonalnie: Usuń nieużywane obiekty Docker
echo "Usuwanie nieużywanych obiektów Docker..."
docker system prune -af

echo "Środowisko Docker zostało wyczyszczone."
