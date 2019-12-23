import Control.Monad
main = do
  xs <- map read . words <$> getLine
  putStrLn $ if solve xs then "win" else "bust"

solve xs = if sum xs <= 21 then True else False
