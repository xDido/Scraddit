import { MoveRight } from "lucide-react";
import { Button } from "../ui/button";
import { Input } from "@/components/ui/input";

export const Hero1 = () => (
  <div className="w-full">
    <div className="container mx-auto">
      <div className="flex gap-8 py-20 lg:py-40 items-center justify-center flex-col">
        <div className="flex gap-4 flex-col">
          <h1 className="text-5xl md:text-7xl max-w-2xl tracking-tighter text-center font-regular">
            Scrappe
          </h1>
          <p className="text-lg md:text-xl leading-relaxed tracking-tight text-muted-foreground max-w-2xl text-center">
            Please enter the subreddit URL or the subreddit name to get the data.
          </p>
        </div>
        <div className="flex flex-row gap-3 w-full max-w-xl">
          <Input
            type="url"
            placeholder="Subreddit URL or name"
            className="flex-1"
          />
          <Button size="lg" className="gap-4">
            Sign up here <MoveRight className="w-4 h-4" />
          </Button>
        </div>
      </div>
    </div>
  </div>
);
