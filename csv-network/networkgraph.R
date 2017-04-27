nodes <- read.csv("nodes.csv",header=T,as.is=T)
links <- read.csv("edge.csv",header=T,as.is=T)
head(nodes)
head(links)
nrow(nodes); length(unique(nodes$id))
nrow(links); nrow(unique(links[,c("from", "to")]))
library('igraph')
net <- graph_from_data_frame(d=links, vertices=nodes, directed=T)
as_edgelist(net, names=T)
as_adjacency_matrix(net, attr="weight")
colrs <- c("gray50", "tomato", "gold")


V(net)$size <- V(net)$size/900
E(net)$width <- E(net)$weight*100
E(net)$arrow.size <- 1

autocurve.edges2 <-function (graph, start = 0.5)
{
    cm <- count.multiple(graph)
    mut <-is.mutual(graph)  #are connections mutual?
    el <- apply(get.edgelist(graph, names = FALSE), 1, paste,
        collapse = ":")
    ord <- order(el)
    res <- numeric(length(ord))
    p <- 1
    while (p <= length(res)) {
        m <- cm[ord[p]]
        mut.obs <-mut[ord[p]] #are the connections mutual for this point?
        idx <- p:(p + m - 1)
        if (m == 1 & mut.obs==FALSE) { #no mutual conn = no curve
            r <- 0
        }
        else {
            r <- seq(-start, start, length = m)
        }
        res[ord[idx]] <- r
        p <- p + m
    }
    res
}

curves <-autocurve.edges2(net)
net.sp <- delete_edges(net, E(net)[weight<0.05])
plot(net.sp, vertex.color="white", edge.curved=curves,layout=layout_randomly)




plot(net, edge.color="gray80", vertex.color="white",layout=layout_randomly)
