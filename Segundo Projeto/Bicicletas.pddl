(define (domain Bicicletas-a)
  (:requirements :strips) 

  (:predicates 
 
   (at ?who ?where)   
   (visitavel ?who ?where)
   (pedalavel ?from ?to)
   (caminhavel ?from ?to)
 
  )
   
        (:action visitar-ponto
    :parameters (?who ?from ?to)   
    :precondition  (and(caminhavel ?from ?to) 
                  (at ?who ?from))         
    :effect (and (not (visitavel ?who ?from))
                 (visitavel ?who ?to))
        )

        (:action caminhar
    :parameters (?who ?from ?to)   
    :precondition  (and(caminhavel ?from ?to) 
                  (at ?who ?from))         
    :effect (and (not (at ?who ?from))
                 (at ?who ?to))
        )

   (:action pedalar
    :parameters (?who ?from ?to)   
    :precondition  (and(pedalavel ?from ?to) 
                  (at ?who ?from))         
    :effect (and (not (at ?who ?from))
                 (at ?who ?to))
        )
    
)