-- 2 variables
main = do
  (x:y:z:xs) <- map read . words <$> getLine
  putStrLn . show $ solve x y z

solve :: Int -> Int -> Int -> Int
solve x y z = min (y `div` x) z
