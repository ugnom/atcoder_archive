import Data.Bits
import qualified Data.ByteString.Char8 as BS
import Control.Monad
import Data.Maybe
import Data.Vector as V hiding (map, replicateM)
import Data.Int

tuplify2 (x:y:_) = (x,y)
tuplify2 _ = undefined

--Input functions with ByteString
readInt = fst . fromJust . BS.readInteger
readIntTuple = tuplify2 . map readInt . BS.words
readIntList = map readInt . BS.words

getInt = readInt <$> BS.getLine
getIntList = readIntList <$> BS.getLine
getIntNList n = map readIntList <$> replicateM (fromIntegral n) BS.getLine
getIntMatrix = map readIntList . BS.lines <$> BS.getContents
getIntTuple = readIntTuple <$> BS.getLine
getIntNTuples n = map readIntTuple <$> replicateM (fromIntegral n) BS.getLine
getIntTuples = map readIntTuple . BS.lines <$> BS.getContents

main = do
  n <- getInt
  xs <- fromList <$> getIntList
  putStrLn . show $ solve n xs

revBitSum x ys = snd $ V.foldr (\y (r,zs) -> ((shiftR r 1), ((r .&. 1) + y) `cons` zs)) (x,empty) ys

--solve :: Int64 -> [Int64] -> Int64
solve n xs =
  let eachBitSum = V.foldr revBitSum (V.replicate 60 0) xs
  in fst $ V.foldr (\x (s,p)-> ((s + p * x * (n-x)) `mod` (10^9 + 7), (p*2) `mod` ((10^9) + 7)) ) (0,1) $ eachBitSum
