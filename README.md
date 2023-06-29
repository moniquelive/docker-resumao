# Exemplo prático do conteúdo sobre Docker

## Como usar este projeto

### Como Compose

```zsh
# Vai gerar a imagem através do Dockerfile e tagea-la.
# Vai expor o phpmyadmin na porta `8080`
# Vai expor o app na porta `9000`
# Vai mapear a pasta atual para a `/app`
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# Vai excluir todos os resursos criados acima
docker compose down
```

### Como Swarm

```zsh
# Para inicializar o swarm
docker swarm init

# Para sair do swarm
docker swarm leave

# Para entrar no swarm
docker swarm join

# Para fazer deploy da stack
docker stack deploy -c docker-compose.yml [nome_da_stack]
```

## Isolado, composto, distribuído

Como instalar? https://docker.com/

Comandos básicos:

- container Manage containers
- image Manage images
- network Manage networks
- system Manage Docker
- volume Manage volumes

### Container

- representam o processo em execução
- sempre possuem um nome (dado ou aleatório)
- 100% isolados do S.O. host (idealmente)
- podem ser executados vários da mesma imagem (mesma ou diferentes versões!)
- podem acessar recursos do S.O. host (gpu, hd, rede, etc)

### Imagem

- representam o conteúdo do "hd" do container
- "read-only" (voláteis)
- baseadas em camadas
- pode partir de outras imagens
- podem ocupar muito espaço
- "registry" = repositórios de imagens
- https://hub.docker.com/

#### Dockerfile[^1]

- Como criar uma imagem baseada em outra
- Como otimizar o tamanho da imagem
- Como criar uma imagem sem se basear em outra
- Como criar uma imagem com um passo de build

#### Build Cache[^2]

- Útil para quando precisar ficar regerando uma mesma imagem
- Cada comando gera uma camada na imagem final
- Quando um comando precisa ser re-executado, o cache dele é invalidado e de todos os comandos seguintes!

### Composição[^3]

- representam a "topologia" da sua rede
- especificam serviços, volumes, redes, configs e secrets que você passaria na CLI
- e pode usá-los para gerar um ambiente de dev ❤️
- para testes locais
- para ambientes de desenvolvimento
- para ci/cd

### Orquestração[^4]

- automatiza o deploy de containers, seu gerenciamento, escala e networking
- exemplos: Docker Swarm, Kubernetes, Apache Mesos
- na nuvem: AWS ECS/EKS, Google GKE, Azure Container Instances

#### Docker Swarm[^5]

- docker swarm -- criar/entrar/sair de um swarm
- docker node -- inspeciona/rm/promove maquinas participantes no swarm
- docker stack -- deploy/ls/rm/services
- docker service -- create/inspect/logs/ls/rm/scale/update

##### Stack[^6]

- funciona logicamente como um docker-compose mas distribuído na rede
- agrupa os serviços necessários para rodar uma aplicação

[^1]: https://docs.docker.com/develop/develop-images/dockerfile_best-practices
[^2]: https://docs.docker.com/build/cache/
[^3]: https://docs.docker.com/compose/compose-file/
[^4]: https://www.redhat.com/en/topics/containers/what-is-container-orchestration
[^5]: https://docs.docker.com/engine/swarm/swarm-tutorial/
[^6]: https://docs.docker.com/engine/swarm/stack-deploy/
