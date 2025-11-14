from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""<nav style="height:50px;padding:22px;background-color:black;color:white;"><center>LET'S ORDER FOR DELIVERY, PICK UP, OR DINE-IN
                        <button style="border-radius:10px;background-color:red;color:white; height:40px; width:130px;">start order</button></center></nav>
                        <div style="height:80px;"></div>
                        <div style="font-size:15px;"><h1 style="margin-left:80px">BROWSE MENU CATEGORIES<h1>
                        <hr style="width:50%; margin-left:45%;margin-top:-30px;"></div>
                        <div style= height:500px; width:52%; "><img style="margin-left:80px;" src='https://images.ctfassets.net/wtodlh47qxpt/wAKmOMcpTm0yfspLrl20B/a49799960b22ba96b733f54971d96825/KFC-category-EPIC-Bucket-1_All-in-one-bucket-delivery_-28th-JAN_1.jpg?fm=webp&fit=fill'><h2 style="height:100px; margin-left:80px; width:470px;"><center>EPIC BUCKET OF THE DAY</center></h2></div>
                        <div style="height:500px;display:grid; list-style:none; grid-template-rows: 250px 250px;grid-template-columns:260px 260px; width:50%; margin-left:49%; margin-top:-500px;">
                        <li><img style="height:180px; width:230px;" src='https://images.ctfassets.net/wtodlh47qxpt/4AcPJzGNNxfXiF1rWvlydj/2a8548a717ff678fbfb0d881b7367ba8/KFC-Gold-Burger-White-Category-23MAY_4.jpg?fm=webp&fit=fill'><p><b><center>GOLD EDITION</center></b></p></li>
                        <li><img style="height:180px; width:230px;"src='https://images.ctfassets.net/wtodlh47qxpt/169o6qKazOgakFLMKkHUGY/d9d657af816a140bdaf3f5a7d64e3ef7/KFC-Veg.jpg?fm=webp'><p><b><center>BOX MEALS</center></b></p></li>
                        <li><img style="height:180px; width:230px;"src='https://images.ctfassets.net/wtodlh47qxpt/5iYMlSgO8gr09Rjbn185qs/8f330ee5eb94ba4eff4f4552e361218d/KFC-Variety-Bucket.jpg?fm=webp&fit=fill'><p><b><center>VARIETY BUCKET</center></b></p></li>
                        <li><img style="height:180px; width:230px;"src='https://images.ctfassets.net/wtodlh47qxpt/169o6qKazOgakFLMKkHUGY/d9d657af816a140bdaf3f5a7d64e3ef7/KFC-Veg.jpg?fm=webp&fit=fill'><p><b><center>VEG</center></b></p></li></div>
                        <div style="height:300px;margin-left:40px; list-style:none; display:grid; grid-template-columns: 300px 300px 300px 300px;">
                        <li><img style="height:200px; width:250px;" src='https://images.ctfassets.net/wtodlh47qxpt/2A4wJjZ8ZvCyj7RSxI3iTk/f403b8ceb2f120bf7ef36d5a913ddf6f/KFC-White-Chicken-Bucket.jpg?fm=webp'><p><b><center>CHICKEN BUCKETS</center></b></p></li>
                        <li><img style="height:200px; width:250px;" src='https://images.ctfassets.net/wtodlh47qxpt/3NdeHBtjjYPHMAoOTpEZ0w/d6c6fadd15bcfa8f6bc969aa02207f0c/KFC-Burger.jpg?fm=webp&fit=fill'><p><b><center>BURGURS</center></b></p></li>
                        <li><img style="height:200px; width:250px;" src='https://images.ctfassets.net/wtodlh47qxpt/5VQAImh8fghx8cYtmjRBxu/050c6b65545546ecca314321a5dddc15/CAT89?fm=webp&fit=fill'><p><b><center>SNACKS</center></b></p></li>
                        <li><img style="height:200px; width:250px;" src='https://images.ctfassets.net/wtodlh47qxpt/7tEmaFwdTOKmVNf724nD21/cb386eac4c508bce817d3daa22a1d3b6/KFC-rice-bowl.jpg?fm=webp&fit=fill'><p><b><center>RICE BOWLZ</center></b></p></li></div>
                        <div style="display:flex; list-style:none; margin-left:40px;gap:50px;">
                             <li><img style="height:200px; width:250px;" src='https://images.ctfassets.net/wtodlh47qxpt/1cS5c1DDcmYuwT0g2edC3f/48712d8b753b8cb6c6abd662398fec70/KFC-Beverages.jpg?fm=webp'><p><b><center>BEVERAGES & DESERT</center></b></p></li>
                             <li><img style="width:850px;"src='https://online.kfc.co.in/static/media/Finger_lickInDesk.a7d05386.svg'</li>
                        </div>
                        <div style="margin-left:40px;"><img src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI5NCIgaGVpZ2h0PSIzMyIgdmlld0JveD0iMCAwIDgwIDQyIiBmaWxsPSJub25lIiBjbGFzcz0iaW5qZWN0ZWQtc3ZnIiBkYXRhLXNyYz0iL3N0YXRpYy9tZWRpYS9TdHJpcGVzX09mZmVyc0ljb24uODkxZTI0YzEuc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CjxyZWN0IHdpZHRoPSIxNi40MTAzIiBoZWlnaHQ9IjQxLjAyNTYiIGZpbGw9IiNFNDAwMkIiPjwvcmVjdD4KPHJlY3QgeD0iMzIuODIwMyIgd2lkdGg9IjE2LjQxMDMiIGhlaWdodD0iNDEuMDI1NiIgZmlsbD0iI0U0MDAyQiI+PC9yZWN0Pgo8cmVjdCB4PSI2My41ODk4IiB3aWR0aD0iMTYuNDEwMyIgaGVpZ2h0PSI0MS4wMjU2IiBmaWxsPSIjRTQwMDJCIj48L3JlY3Q+Cjwvc3ZnPg=='></div>
                        <h1 style="margin-left:40px; font-size:35px; font-weight:900;">Save More as you order</h1>
                        <div style="display:flex;justify-content:center; gap:20px;">
                        <div style="width:350px; height:450px;"><img style="height:200px; width:350px;" src='https://orderserv-kfc-assets.yum.com/15895bb59f7b4bb588ee933f8cd5344a/images/offers/lg/CHKZINGER.jpg?ver=73.53' ><h2 style="text-align:center;">FREE CLASIC ZINGER</h2><p style="text-align:center;">min.order value 499</p><p style="text-align:center;">view details</p><br><center><button style="height:40px; width:100px; border-radius:10px; background-color:black; color:white;">Apply offer</button></center></div>
                        <div style="width:350px; height:450px;"><img style="height:200px; width:350px;" src='https://orderserv-kfc-assets.yum.com/15895bb59f7b4bb588ee933f8cd5344a/images/offers/lg/ADDCHK99.jpg?ver=73.53' ><h2 style="text-align:center;">2PC HOT & CRISPY CHICKEN @ RS 99</h2><p style="text-align:center;">min.order value 499</p><p style="text-align:center;">view details</p><br><center><button style="height:40px; width:100px; border-radius:10px; background-color:black; color:white;">Apply offer</button></center></div>
                        <div style="width:350px; height:450px;"><img style="height:200px; width:350px;" src='https://orderserv-kfc-assets.yum.com/15895bb59f7b4bb588ee933f8cd5344a/images/offers/lg/BIGSAVE.jpg?ver=73.53' ><h2 style="text-align:center;">UPTO RS 100 OFF</h2><p style="text-align:center;">min.order value 699</p><p style="text-align:center;">view details</p><br><center><button style="height:40px; width:100px; border-radius:10px; background-color:black; color:white;">Apply offer</button></center></div>
                        </div>
                        <footer style="background-color:black; height:25rem; padding:5rem;">
        <div style=" height:25rem; align-items:center;">
            <div style="height:90%; width:95%; display:flex; justify-content:center; align-items:center;">
                <div style="height:90%; width:13%;">
                    <img src="https://images.ctfassets.net/wtodlh47qxpt/25FSYFuEtGct8NSrtpKe6d/b602f6fe0bf294e6a6dff5d7648bf594/KFC_Logo.svg?h=120&w=120&fm=webp&fit=fill" style="width:4rem;">
                </div>
                <div style="height:90%; width:13%; color:white; font-size:15px;">
                    <h1 style="font-size:14px; margin-bottom:8px;">KFC India</h1>
                    <span>About KFC</span><br>
                    <span>KFC Care</span><br>
                    <span>Careers</span><br>
                    <span>Our Golden Past</span><br>
                    <span>Responsible</span><br>
                    <span>Disclosure</span><br>
                </div>
                         <div style="height:90%; width:13%; color:white; font-size:15px;">
                    <h1 style="font-size:14px; margin-bottom:8px;">Legal</h1>
                    <span>Terms and</span><br>
                    <span>Condition</span><br>
                    <span>Privacy Policy</span><br>
                    <span>Disclaimer</span><br>
                    <span>Caution Notice</span><br>
                </div>
                <div style="height:90%; width:13%; color:white; font-size:15px;">
                 <h1 style="font-size:14px; margin-bottom:8px;">KFC Food</h1>
                    <span>Menu</span><br>
                    <span>Order Lookup</span><br>
                    <span>Gift Card</span><br>
                    <span>Nutrition &</span><br>
                    <span>Allergen</span><br>
                </div>
                     <div style="height:90%; width:13%; color:white; font-size:15px;">
                    <h1 style="font-size:14px; margin-bottom:8px;">Support</h1>
                    <span>Get Help</span><br>
                    <span>Contact</span><br>
                    <span>KFC Feedback</span><br>
                    <span>Privacy Policy</span><br>
                </div>
                <div style="height:90%; width:13%; color:white; font-size:15px;">
                    <span><img src="https://images.ctfassets.net/wtodlh47qxpt/6qgKpWUOIsrIiazhk3cdmF/d60b4c20be69bab1f939bf33348b67e9/Find_KFC.svg?h=15&w=11&fm=webp&fit=fill">  Find a KFC</span>
                </div>
            </div>
            <div style="color:white; display:flex; justify-content:center; height:10%; font-size:small;">
                Copyright © KFC Corporation 2025 All rights reserved build pwa-2504-0-9_53cdc423
            </div>
        </div>
    </footer>
   


                        """)
