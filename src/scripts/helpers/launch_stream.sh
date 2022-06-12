#!/bin/bash

ID=$1

OPTIONSEMITTER="$2"
OPTIONSCONSUMER="$3"

#Necesario para nvidia
#docker exec fis-hubu-consumer-$ID rmmod nvidia_drm && rmmod nvidia_modeset && rmmod nvidia_uvm && rmmod nvidia && modprobe nvidia && modprobe nvidia_uvm && modprobe nvidia_modeset

#docker exec -d fis-hubu-consumer-$ID /bin/bash -c "cd app && /root/miniconda3/envs/default-conda/bin/python consumer.py  ...
docker exec -d fis-hubu-consumer-$ID /bin/bash -c "cd app && /root/miniconda3/envs/default-conda/bin/python consumer.py --kafkahost='kafka_kafka_1:29092' --output=/mnt/data --topic=video-stream-patient-$ID --sparkhost='spark://spark-master-fishubu:7077' $OPTIONSCONSUMER > /mnt/data/log-$ID 2> /mnt/data/log-error-$ID"
echo 'Lanzado consumidor'
docker exec -d fis-hubu-productor-$ID /bin/bash -c "cd app && /root/miniconda3/envs/default-conda/bin/python producer.py --port=12345 --kafkahost='kafka_kafka_1:29092' --topic=video-stream-patient-$ID"
echo 'Lanzado productor'

#Añadido Lucía
container_id=$(docker ps --filter name=fis-hubu-productor-0 --format {{.ID}})
echo "$container_id"
#Vamos a asignarle más memoria
#docker update --memory "8g" --cpuset-cpu "4" $container_id
#Muevo el archivo dentro del Docker
docker cp /home/lnc1002/processed/Ejercicio1-2.mp4 $container_id:/Ejercicio1-2.mp4
#docker cp /home/lnc1002/processed/1597651245-2.webm docker ps --filter "name=fis-hubu-productor-0" --format "{{.ID}}":/
 
#docker exec -d fis-hubu-productor-$ID /bin/bash -c "cd app && /root/miniconda3/envs/default-conda/bin/python emitter.py --port=12345 --file=/app/testvideos/sentado2-cruzado.mp4 $OPTIONSEMITTER"
docker exec -d fis-hubu-productor-$ID /bin/bash -c "cd app && /root/miniconda3/envs/default-conda/bin/python emitter.py --port=12345 --file=/Ejercicio1-2.mp4 $OPTIONSEMITTER"
echo 'Lanzado emisor para test'




