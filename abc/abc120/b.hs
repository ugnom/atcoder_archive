-- 2 variables
main = do
  (x:y:k:xs) <- map read . words <$> getLine
  putStrLn . show $ solve x y k (min x y)

solve :: Int -> Int -> Int -> Int -> Int
solve x y k p
  | x `mod` p == 0 && y `mod` p == 0 =
      if k == 1 then
        p
      else
        solve x y (k-1) (p-1)
  | otherwise = solve x y k (p-1)
