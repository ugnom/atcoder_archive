import Control.Monad
import Data.List

main = do
  n <- read <$> getLine
  xs <- forM [1..n] $ \t -> do
    a <- read <$> getLine
    ys <- forM [1..a] $ \u -> do
      (x:y:yy) <- map read . words <$> getLine
      return (x,y)
    return . compose n 1 $ (sort ys)
  --putStrLn . show $ xs
  putStrLn . show $ solve n xs


compose :: Int -> Int -> [(Int,Int)] -> [Int]
compose n k [] = if n < k then [] else (-1):(compose n (k+1) [])
compose n k all@((x,y):xs) = if k == x then y:(compose n (k+1) xs) else (-1):(compose n (k+1) all)

solve :: Int -> [[Int]] -> Int
solve n xs =
  let comb = replicateM n [0,1]
      filtered = filter (calc' xs (replicate n (-1))) comb
  in maximum $ map (length . filter (== 1)) filtered

calc' xs ys zs = calc zs xs ys zs

calc :: [Int] -> [[Int]] -> [Int] -> [Int] -> Bool
calc ks [] ys [] = True
calc ks (x:xs) ys (z:zs) =
  if z == 0 then
    calc ks xs ys zs
  else
    if (and (map (\(xi,y) -> xi == y  || y == -1 || xi == -1) (zip x ys))) && (and (map (\(k,xi) -> xi == -1 || k == xi) (zip ks x))) then
      calc ks xs (map (\(xi,y) -> if y == -1 then xi else y) (zip x ys)) zs
    else
      False
