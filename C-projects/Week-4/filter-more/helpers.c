#include "helpers.h"
#include <math.h>
#include <cs50.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int red, green, blue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //get colur values of pixel
            red = image[i][j].rgbtRed;
            green = image[i][j].rgbtGreen;
            blue = image[i][j].rgbtBlue;
            //get the average
            int average = round((red + green + blue) / 3.0);
            //assign the value again
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        //if thr result of width mod 2 = 0
        if (width % 2 == 0)
        {
            //for loop to take pixel and replace it
            for (int j = 0; j < width / 2; j++)
            {
                RGBTRIPLE temp[height][width];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j];
            }
        }
        //other wise if no. of pixels is even
        else
        {
            //for loop to take pixel and replace it
            for (int j = 0; j < (width - 1) / 2; j++)
            {
                RGBTRIPLE temp[height][width];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][width - (j + 1)];
                image[i][width - (j + 1)] = temp[i][j];
            }
        }
    }
    return;

}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            temp[i][j] = image[i][j];
            float totalr, totalg, totalb;
            totalr = 0;
            totalg = 0;
            totalb = 0;
            float counter = 0.00;
            //make 3x3
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentx = i + x;
                    int currenty = j + y;
                    //check if pixel is valid
                    //if (( currentx < 0 || currentx > (height - 1)) && (( currenty < 0) || currenty > (width - 1)))
                    //{
                    //continue;
                    //}
                    if (currentx < 0 || currentx > height - 1)
                    {
                        continue;
                    }

                    if (currenty < 0 || currenty > width - 1)
                    {
                        continue;
                    }
                    //get value
                    totalr += image[currentx][currenty].rgbtRed;
                    totalg += image[currentx][currenty].rgbtGreen;
                    totalb += image[currentx][currenty].rgbtBlue;
                    counter++;
                }

            }
            //calculate average
            temp[i][j].rgbtRed = round(totalr / counter);
            temp[i][j].rgbtGreen = round(totalg / counter) ;
            temp[i][j].rgbtBlue = round(totalb / counter);
        }
    }
    //copy all new values to pixels' rgb
    for (int i = 0; i < height ; i++)
    {
        for (int j = 0; j < height ; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};
    //make 3x3
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            temp[i][j] = image[i][j];
            int gxr = 0;
            int gyr = 0;
            int gxg = 0;
            int gyg = 0;
            int gxb = 0;
            int gyb = 0;
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentx = i + x;
                    int currenty = j + y;
                    //check if pixel is valid
                    if (currentx < 0 || currentx > height - 1)
                    {
                        continue;
                    }
                    if (currenty < 0 || currenty > width - 1)
                    {
                        continue;
                    }
                    //multibly rgb values with gx and gy
                    gxr += image[currentx][currenty].rgbtRed * gx[x + 1][y + 1];
                    gyr += image[currentx][currenty].rgbtRed * gy[x + 1][y + 1];
                    gxg += image[currentx][currenty].rgbtGreen * gx[x + 1][y + 1];
                    gyg += image[currentx][currenty].rgbtGreen * gy[x + 1][y + 1];
                    gxb += image[currentx][currenty].rgbtBlue * gx[x + 1][y + 1];
                    gyb += image[currentx][currenty].rgbtBlue * gy[x + 1][y + 1];

                }
            }
            //calculate square root of gx and gy of each color
            int red = round(sqrt((gxr * gxr) + (gyr * gyr)));
            int green = round(sqrt((gxg * gxg) + (gyg * gyg)));
            int blue = round(sqrt((gxb * gxb) + (gyb * gyb)));
            //if the value is greater than 255 make it 255 to each color
            if (red > 255)
            {
                red = 255;
            }
            if (green > 255)
            {
                green = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            //copy values of rgb to temp rgb
            temp[i][j].rgbtRed = red;
            temp[i][j].rgbtGreen = green;
            temp[i][j].rgbtBlue = blue;
        }
    }
    //copy all new values to pixels' rgb
    for (int i = 0; i < height ; i++)
    {
        for (int j = 0; j < height ; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
    return;
}
