select distinct pot1.email from person pot1, person pot2 where pot2.email = pot1.email AND pot2.id<>pot1.id
