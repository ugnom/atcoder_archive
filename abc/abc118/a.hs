main = do
  (x:y:xs) <- map read . words <$> getLine
  putStrLn . show $ solve' x y

solve' :: Int -> Int -> Int
solve' a b = if b `mod` a == 0 then a+b else b-a
