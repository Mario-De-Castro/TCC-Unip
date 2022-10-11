import { Fires } from './fires';
export interface LocalData {
  count: number;
  next: string | null;
  previous: string | null;
  results: Fires[];
}
