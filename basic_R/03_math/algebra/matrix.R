check_idempotent <- function(M, tol = 1e-9) {

    M <- as.matrix(M)
    nr <- nrow(M)
    nc <- ncol(M)

    if (nr != nc) {
        cat("đéo vuông nên đéo care\n")
        return(0)
    }

    M2 <- M %*% M
    diff <- M2 - M

    if (all(abs(diff) < tol)) {
        cat("Lũy đẳng\n")
        return(1)
    } else {
        cat("vuông nhưng đéo lũy đẳng\n")
        return(0)
    }
}

check_orthogonal <- function(M, tol = 1e-9) {

    M <- as.matrix(M)

    if (nrow(M) != ncol(M)) {
        cat("Not square → cannot be orthogonal\n")
        return(0)
    }

    I <- diag(nrow(M))
    diff <- t(M) %*% M - I

    if (all(abs(diff) < tol)) {
        cat("Orthogonal\n")
        return(1)
    } else {
        cat("Not orthogonal\n")
        return(0)
    }
}

check_positive_definite <- function(M) {

    M <- as.matrix(M)

    # symmetric check
    if (!isTRUE(all.equal(M, t(M)))) {
        cat("Not symmetric → cannot be positive definite\n")
        return(0)
    }

    eigvals <- eigen(M, symmetric = TRUE)$values

    if (all(eigvals > 1e-12)) {
        cat("Positive definite\n")
        return(1)
    } else {
        cat("Not positive definite\n")
        return(0)
    }
}

check_idempotent(matrix(c(1,0,0,1), 2, 2))
check_orthogonal(matrix(c(0,1,1,0), 2, 2))
check_positive_definite(matrix(c(2,-1,-1,2), 2, 2))