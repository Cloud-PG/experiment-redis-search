# experiment-redis-search
Experimenting with Redis search for data analysis

#ENG

This is a docker image for build a redisearch cluster.
Running this file you will able to use a redisearch cluster. This cluster is compsed by 6 nodes, three masters and three slaves.

For start the cluster explore the right directory:

cd experiment-redis-search-master


then you can build the image with:

docker-compose build


and then you can run the conteiner with:

docker-compose up

or 

docker-compose up -d

the second option will run the conteiner as a daemon.


For access to the cluster as a client use the command:

redis-cli -c -p 7000

you can change the port-number, the number accepted are from 7000 to 7005.

Now you can use this cluster using redisearch module.


#ITA

Questo è un'immagine docker per la costruzione di un cluster redisearch.
Eseguendo il file potrai usare un cluster redisearch. Questo cluster è composto da 6 nodi, 3 master e 3 slave.

Per far partire il cluster bisogna prima esplorare la directory giusta:

cd experiment-redis-search-master


Poi puoi costruire l'immagine con:

docker-compose build


Quindi puoi eseguire il conteiner con

docker-compose up

o

docker-compose up -d

la seconda opzione eseguirà il conteiner come demone.


Per accedere al cluster come client, usa il comando:

redis-cli -c -p 7000

si può cambiare il port-number, i numeri accettati vanno da 7000 a 7005.

Ora puoi usare questo cluster con il modulo redisearch.
