main :: IO ()
main = do
  (x:y:xs) <- map read . words <$> getLine
  putStrLn $ if solve' x y then "YES" else "NO"

solve' :: Int -> Int -> Bool
solve' x y = (x+1) `div` y >= 2
