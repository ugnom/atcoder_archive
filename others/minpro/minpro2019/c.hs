main = do
  (k:a:b:xs) <- map read . words <$> getLine
  putStrLn . show $ solve' k a b

solve' :: Integer -> Integer -> Integer -> Integer
solve' k a b
  | b - a <= 2 || k - (a - 1) <= 0 = k + 1
  | otherwise = let k1 = k - (a - 1)
                in (b - a) * (k1 `div` 2) + (k1 `mod` 2) + a
