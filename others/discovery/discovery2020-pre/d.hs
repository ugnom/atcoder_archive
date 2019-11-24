
compress d c =
  let nsteps = steps 0 d d
      (x,k) = step (d `mod` nsteps) 0 d d
  in (x + (nsteps * ))

step 0 k x d = (x,k)
step n k x d
  | x > 9 = step n (k+1) (sum . amp (read . return) . show $ x) d
  | otherwise = step (n-1) (k+1) (x+d) d

steps :: Int -> Int -> Int -> Int
steps n k x d
  | x == d && n /= 0 = n
  | x > 9 = steps (n+1) (sum . map (read . return) . show $ x) d
  | otherwise = steps (n+1) (x+d) d
